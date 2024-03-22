library(tidyverse)
library(janitor)

date_of_export <- "20240318"


# Load Bank & YNAB Transactions -------------------------------------------
bank_transactions <- read.csv(paste0("H:/Misc/personal/bank activity/chase_checking_activity_", date_of_export, ".csv")) %>% 
  clean_names() %>% 
  as_tibble() %>% 
  mutate(outflow = amount*-1) %>% 
  select(posting_date, description, outflow) %>% 
  mutate(posting_date = mdy(posting_date)) %>% 
  filter(posting_date >= ymd("2022-03-18"),
         posting_date < ymd("2024-03-18")) %>%
  arrange(desc(posting_date)) %>% 
  rename(date = posting_date) %>%
  mutate(id = 1:n()) %>% 
  # remove payments 
  filter(outflow > 0 ) %>% 
  # remove flagstar payments 
  mutate(flag_star = str_detect(description, "FLAGSTAR")) %>% 
  filter(!flag_star)

ynab_transactions <- read.csv(paste0("H:/Misc/personal/ynab/register_", date_of_export, ".csv")) %>% 
  filter(Account == "Chase Checking") %>% 
  clean_names() %>% 
  as_tibble() %>% 
  mutate(split_transaction_flag = str_detect(memo, "Split")) %>% 
  mutate(outflow = as.numeric(gsub("[:$:]", "", outflow)),
         inflow = as.numeric(gsub("[:$:]", "", inflow))) %>% 
  # remove payments
  filter(inflow == 0) %>% 
  # remove flagstar payments
  mutate(flag_star = str_detect(payee, "Flagstar"),
         equity = str_detect(payee, "Equity")) %>% 
  filter(!flag_star,
         !equity) %>% 
  # keep only transactions from march 18 2022 to yesterday
  mutate(date = mdy(date)) %>% 
  filter(date >= ymd("2022-03-18"),
         date < ymd("2024-03-18")) 

# Reformat YNAB Transactions ----------------------------------------------
split_transactions_only <- ynab_transactions %>% 
  filter(split_transaction_flag) %>% 
  group_by(date, payee) %>% 
  mutate(total_outflow = sum(outflow)) %>% 
  ungroup() %>% 
  select(date, payee, total_outflow, split_transaction_flag) %>% 
  rename(outflow = total_outflow) %>% 
  distinct()

tidy_transactions <- ynab_transactions %>% 
  filter(!split_transaction_flag) %>% 
  select(date, payee, outflow, inflow, split_transaction_flag) %>% 
  bind_rows(split_transactions_only) %>% 
  mutate(inflow = ifelse(is.na(inflow), 0, inflow))

# Review Duplicate Transactions -------------------------------------------

# check for duplicate transactions in bank statement
# note: dups have been verified in chase.
bank_duplicates <- bank_transactions %>% 
  group_by(date) %>% 
  count(outflow) %>% 
  filter(n > 1) %>% 
  ungroup()

# check for duplicate transactions in ynab statement
# one needed to be manually corrected to but was verfied to match the 
# bank
ynab_duplicates <- tidy_transactions %>% 
  filter(outflow != 0 ) %>% 
  group_by(date) %>% 
  count(outflow) %>% 
  ungroup() %>% 
  filter(n > 1) 

(dup_comparison <- ynab_duplicates %>% 
  # select(-date) %>% 
  mutate(ynab = T) %>% 
  full_join(bank_duplicates %>% 
              mutate(bank = T)) %>% 
  select(date, outflow, bank, ynab))

# remove true duplicates that match between ynab and the bank so that
# we can identify incorrect duplicate transactions
verified_dups <- dup_comparison %>% 
  filter(bank & ynab) %>% 
  mutate(delete = T)

# Compare Transactions ----------------------------------------------------
ynab_deduped <- tidy_transactions %>% 
  # removed duplicates that have already been reviewed
  left_join(verified_dups %>% 
              select(date, outflow, delete)) %>% 
  mutate(delete = ifelse(is.na(delete), F, delete)) %>% 
  filter(!delete) %>% 
  select(-delete)

bank_deduped <- bank_transactions %>% 
  # removed duplicates that have already been reviewed
  left_join(verified_dups %>% 
              select(date, outflow, delete)) %>% 
  mutate(delete = ifelse(is.na(delete), F, delete)) %>% 
  filter(!delete) %>% 
  select(-delete)

# match transactions 
date_match <- ynab_deduped %>% 
  left_join(bank_deduped) %>% 
  arrange(date, outflow) 

missing_match <- date_match %>% 
  filter(is.na(id))

nrow(missing_match)

missing_match %>% 
  mutate(date = date + days(3)) %>% 
  select(colnames(ynab_deduped)) %>% 
  left_join(bank_deduped) %>% 
  filter(is.na(id)) %>% 
  count()


# match sure that there are no ids repeated more than once
transaction_comparison %>% 
  count(id) %>% 
  filter(n > 1)

