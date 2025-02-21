from crontab import CronTab


class Scheduler:
    """ This class is responsible for adding the below scripts into RPi's crontab"""

    @staticmethod
    def run_script():
        pi_cron = CronTab(user='pi')
        # Clear all previous cronjobs if any exists
        pi_cron.remove_all()

        # Schedule the monitor app to run every minute
        schedule_monitor = pi_cron.new(
            command="cd /home/pi/Desktop/IoT && /home/pi/miniconda3/envs/venv/bin/python3.5 monitorAndNotify.py")
        schedule_monitor.minute.every(1)

        # Schedule bluetooth app to run every 5 minute
        schedule_bluetooth = pi_cron.new(
            command="cd /home/pi/Desktop/IoT && /home/pi/miniconda3/envs/venv/bin/python3.5 bluetooth_messenger.py")
        schedule_bluetooth.minute.every(5)

        # Schedule to create reports at 23:56 every day
        schedule_report = pi_cron.new(
            command="cd /home/pi/Desktop/IoT && /home/pi/miniconda3/envs/venv/bin/python3.5 createReport.py")
        schedule_report.setall('56 23 * * *')

        # Create plots at 23:59 every day
        schedule_analytics = pi_cron.new(
            command="cd /home/pi/Desktop/IoT && /home/pi/miniconda3/envs/venv/bin/python3.5 analytics.py")
        schedule_analytics.setall('59 23 * * *')

        pi_cron.write()


if __name__ == '__main__':
    Scheduler.run_script()
