
multi <- function(x, y) {
  return(x + y)
  print(paste(x + y))
}
multi(2, 3)

for (i in 1:5) {
  print(i)
}

i <- 1
while (i <- 10) {
  i <- i + 1
  print(i)
}

i <- 1
add_fun <- function(b) {
  b
}
# lapply(i in 1:i+9, add_fun)

sapply(0:4, function(a) {
  a + 1
})

sapply(0:10, function(b) {
  b + 10
})

good_day <- function(code_working, day) {
  if (code_working == TRUE && day == "Friday") {
    "BEST. DAY. EVER. Stop while you are ahead and go to the pub!"
  } else if (code_working == FALSE && day == "Friday") {
    "Oh well, but at least it's Friday! Pub time!"
  } else if (code_working == TRUE && day != "Friday") {
    "So close to a good day... shame it's not a Friday"
  } else if (code_working == FALSE && day != "Friday") {
    "Hello darkness."
  }
}
good.day(code.working = FALSE, day = "Monday")


eggs <- TRUE
if (eggs == TRUE) {
  n_milk <- 6
} else {
  n_milk <- 0
}

n_milk

i <- 9
for (i in 1:i + 1) {
  print(i)
}

star <- c()
for (i in 1:5) {
  for (j in 1:i + 1) {
    star <- c(star, "*")
    cat("*")
  }
  cat("\n")
  star <- c()
}
val <- switch(1,
  "Geeks1",
  "Geeks2",
  "Geeks3",
  "Geeks4",
  "Geeks5",
  "Geeks6"
)
print(val)