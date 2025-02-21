from json_parser import Parser


class Checker:
    """This class will take temperature and humidity and determine if they are within range and send back appropriate
    response"""
    @staticmethod
    def check_temperature(temperature):
        # Get data from parser
        data = Parser.get_instance()
        # Compare data
        if temperature < data.min_temperature:
            status = 'BAD'
            report = '{}*C below minimum temperature.'.format(round(data.min_temperature - temperature, 2))
            return status + ': ' + report
        if temperature > data.max_temperature:
            status = 'BAD'
            report = '{}*C above maximum temperature.'.format(round(temperature - data.max_temperature, 2))
            return status + ': ' + report
        return 'OK. Current temperature is within range'

    @staticmethod
    def check_humidity(humidity):
        data = Parser.get_instance()
        if humidity < data.min_humidity:
            status = 'BAD'
            report = '{}% below minimum humidity.'.format(round(data.min_humidity - humidity, 2))
            return status + ': ' + report
        if humidity > data.max_humidity:
            status = 'BAD'
            report = '{}% above maximum humidity.'.format(round(humidity - data.max_humidity, 2))
            return status + ': ' + report
        return 'OK. Current humidity is within range'
