library(ggplot2)
library(dplyr)

pub_date <- read.csv("pub_date.csv")
pub_date |>
    filter(year >= 2004) |>
    ggplot(aes(year, count)) +
    geom_line() +
    theme(strip.background = element_blank(), strip.placement = "outside")

ggsave("data/pub_date.pdf")

