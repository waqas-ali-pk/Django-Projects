import datetime

def test_cron_job():
    print("cron job started successfully", datetime.datetime.now())
    f = open('test_cron_job_file.txt', 'w')
    f.close()
    print("cron job completed successfully")