# Load Packages -----------------------------------------------------------
library(googlesheets4)
library(janitor)
library(tidyverse) 

# Load in Data ------------------------------------------------------------
zos_poll_responses <- read_sheet(ss = "https://docs.google.com/spreadsheets/d/1yUwELjF__WB2PZCX4koycDI7oGx_AOBnZgbAzG9Zufw/edit#gid=0",
           sheet = 1) %>% 
  clean_names() %>% 
  rename(n = value) %>%
  mutate(response = as.character(response))

# Create Count Function ---------------------------------------------------
zos_estimates <- function(data = zos_poll_responses, question){
  data %>% 
    filter(q_number == question) %>% 
    mutate(total_responses = sum(n)) %>% 
    mutate(percent = n/total_responses) %>% 
    select(response, total_responses, n, percent)
}

# Examine Total Responses -------------------------------------------------
# how many responses did each question get? note that Mayra did not collect 
# responses for q8) pros and cons about instagram 
(response_count <- zos_poll_responses %>% 
  group_by(q_number) %>% 
  mutate(total_response = sum(n)) %>% 
  ungroup() %>% 
  select(q_number, metric, total_response) %>% 
  distinct() %>% 
  arrange(desc(total_response)))

# what was the rang of responses per question?
summary(na.omit(response_count$total_response))

# Look at Instagram Users Data --------------------------------------------
## Q7) Do you use IG more for sharing content or viewing others' content?
(q7_counts <- zos_estimates(question = 7))
# A tibble: 2 x 4
#   response total_responses     n percent
#   <chr>              <dbl> <dbl>   <dbl>
# 1 Sharing               96    47   0.490
# 2 Viewing               96    49   0.510

## Q1) Instagram your main social media app of choice? 
(q1_counts <- zos_estimates(question = 1))
# A tibble: 2 x 4
#   response total_responses     n percent
#   <chr>              <dbl> <dbl>   <dbl>
# 1 Yes                  175   131   0.749
# 2 No                   175    44   0.251

## Q2) What time of day do you use it?
(q2_counts <- zos_estimates(question = 2))
# A tibble: 4 x 4
#   response  total_responses     n percent
#   <chr>               <dbl> <dbl>   <dbl>
# 1 All day               155   102  0.658 
# 2 Morning               155    19  0.123 
# 3 Afternoon             155    19  0.123 
# 4 Night                 155    15  0.0968

## Q3) How many hours per day do you spend on IG?
q3_counts <- zos_poll_responses %>%
  filter(q_number == 3) %>%
  # remove string responses
  mutate(response = as.numeric(response)) %>%
  # remove unrealistic responses, hours are more than hours in a day
  mutate(response = ifelse(response > 24, NA, response),
         n = ifelse(is.na(response), NA, n)) %>%
  filter(!is.na(n)) %>%
  zos_estimates(question = 3)

# examine the distribution by time
q3_counts %>% 
  add_row(response = 4.5, total_responses = 51, n = 0, percent = 0) %>% 
  add_row(response = 5.5, total_responses = 51, n = 0, percent = 0) %>% 
  add_row(response = 7, total_responses = 51, n = 0, percent = 0) %>% 
  add_row(response = 7.5, total_responses = 51, n = 0, percent = 0) %>% 
  add_row(response = 8, total_responses = 51, n = 0, percent = 0) %>% 
  add_row(response = 8.5, total_responses = 51, n = 0, percent = 0) %>% 
  add_row(response = 9, total_responses = 51, n = 0, percent = 0) %>% 
  add_row(response = 9.5, total_responses = 51, n = 0, percent = 0) %>% 
  add_row(response = 10, total_responses = 51, n = 0, percent = 0) %>% 
  add_row(response = 10.5, total_responses = 51, n = 0, percent = 0) %>% 
  add_row(response = 11, total_responses = 51, n = 0, percent = 0) %>% 
  add_row(response = 11.5, total_responses = 51, n = 0, percent = 0) %>% 
  mutate(
    response = as.character(response),
    response = as.factor(response),
    response = factor(response, levels = c(0, 0.25, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5,
                                           5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10,
                                           10.5, 11, 11.5, 12))) %>% 
  arrange(response) %>% 
  ggplot(aes(x = response, y = n)) +
  geom_bar(stat = "identity") +
  theme_minimal()

# examine how many people number of hours by three groups
(q3_3categories <- q3_counts %>% 
  mutate(response = case_when(
    response <= 2 ~ "2 hours or less",
    response > 2 & response < 6 ~ "2 to 5.5 hours",
    response >= 6 ~ "6+ hours"
  )) %>% 
  group_by(response) %>% 
  summarize(n = sum(n)) %>% 
  ungroup()) %>% 
  mutate(
    total_responses = sum(n), 
    percent = n/total_responses,
    response = as.factor(response),
    response = factor(response, levels = c("2 hours or less",
                                           "2 to 5.5 hours",
                                           "6+ hours"))) %>% 
  arrange(response)
# A tibble: 3 x 2
#   response3                          n
#   <chr>                          <dbl>
# 1 2 hours or less                   31
# 2 More than 2 hours, less than 6    15
# 3 6+ hours                           5