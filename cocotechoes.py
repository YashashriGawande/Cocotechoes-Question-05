import random
from datetime import datetime, timedelta

class Task:
    def __init__(self, name, progress):
        self.name = name
        self.progress = progress

class Job:
    def __init__(self, title):
        self.title = title
        self.tasks = []
        self.end_date = datetime.now() + timedelta(days=random.randint(1, 30))

def generate_random_jobs(num_jobs):
    jobs = [Job(f"Job{i}") for i in range(1, num_jobs + 1)]
    for job in jobs:
        job.tasks = [Task(f"Task{j}", random.randint(0, 100)) for j in range(1, random.randint(10, 20))]
    return jobs

def calculate_overall_progress(job):
    return sum(task.progress for task in job.tasks) / len(job.tasks) if job.tasks else 0

def main():
    random.seed()
    num_jobs = 10
    random_jobs = generate_random_jobs(num_jobs)
    
    sorted_jobs = sorted(random_jobs, key=lambda job: (job.end_date, -calculate_overall_progress(job)))
    
    print("Sorted Jobs:")
    for job in sorted_jobs:
        print(f"{job.title} - End Date: {job.end_date.strftime('%Y-%m-%d')} | Overall Progress: {calculate_overall_progress(job):.2%}")

if __name__ == "__main__":
    main()
 