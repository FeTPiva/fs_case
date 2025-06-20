# iFood ML Engineer Test · Feature Store

In this exercise, you will build a straightforward feature store, which provides both real-time and historical data for machine learning. This is crucial for training and serving models with consistent, reliable, and flexible data.


## 1. Feature Store Construction

### Objective:
- Design a system that ingests data from streaming sources, aggregates features, and serves them both offline (for model training) and online (for real-time inference).
- Maintain data consistency (avoiding data loss), ensure scalability, and provide low latency for online predictions.

### Data Sources:
You have four files to treat as streaming inputs:
1. order.json.gz → https://data-architect-test-source.s3-sa-east-1.amazonaws.com/order.json.gz
2. consumer.csv.gz → https://data-architect-test-source.s3-sa-east-1.amazonaws.com/consumer.csv.gz
3. restaurant.csv.gz → https://data-architect-test-source.s3-sa-east-1.amazonaws.com/restaurant.csv.gz
4. status.json.gz → https://data-architect-test-source.s3-sa-east-1.amazonaws.com/status.json.gz

### Requirements:
- Emulate a streaming source using these files.
- No data loss; the pipeline must be consistent.
- Scalable design (able to handle increasing or variable data volume).
- Real-time aggregation of data (e.g., computing rolling features, last-known status, etc.).
- Both offline (batch) and online (real-time) storage/serving of features.

### Deliverable:
- A runnable solution (Docker image, Docker Compose, scripts, or notebooks) that starts reading the files, processes them, and stores the results in a structured format.
- A clear README describing how to run your solution. Example steps might include:
  1. “Run docker-compose up --build”
  2. “Check logs to see the pipeline”
  3. “Access data outputs at /path/to/output for offline usage”
  4. “Hit localhost:8000/features?id=XYZ for real-time features”

## 2. AWS Infrastructure

### Objective

Demonstrate AWS proficiency by proposing a reliable, scalable, and cost-efficient architecture for your solution.

### What to do

- Propose a reliable, scalable, and cost-effective AWS infrastructure.
- A simple diagram or list of AWS services will suffice, but you can include code or configuration snippets if you prefer.


### Deliverable

- A short document (1–2 pages or less) describing your design decisions and how each AWS service fits together.


## 4. Bonus Challenges (Optional)

The following puzzles are purely for fun. They are not part of the official evaluation.

### Level 1 & Level 2
Inside the “bonus” folder, there are two binaries: `level01` and `level02`. Each one has a password.
- Can you figure out the passwords for these binaries without source code?

### Level 3
There is another binary called `level03`.
- Can you find a way to execute a shell from this binary?

Example:
$ ./bonus/level03
[+] calling some crazy function, can you get a shell?
password: [some_input_that_results_in_/bin/sh_execution]
$ echo "Habemus shell!"


## Submission Guidelines

1. Upload your code, diagrams, or documents to a repository or zip file.
2. Provide instructions in a README to help us run and test everything easily.
3. If you completed the bonus challenges, make sure to show how you solved them (or just explain your process).

Thank you for your time and effort in completing this test! We look forward to reviewing your work.