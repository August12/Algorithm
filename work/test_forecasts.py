import unittest
from pyspark import SparkContext, SQLContext
from forecasts import forecastsCommand


class forecastsTests(unittest.TestCase):

    sqlCtx = None

    @classmethod
    def setUpClass(cls):
        """Do seting up class for test."""
        forecastsTests.sc = SparkContext('local' )#spark://192.168.100.180:9090
        forecastsTests.sqlCtx = SQLContext(forecastsTests.sc)
        forecastsTests.version = str(forecastsTests.sqlCtx._sc.version)
        
        data = [
                ['20181029192000', 'host', 20], ['20181029192010', 'host', 25], ['20181029192020', 'host', 30],
                ['20181029192030', 'host', 35], ['20181029192040', 'host', 40], ['20181029192050', 'host', 45],
                ['20181029192100', 'host', 50], ['20181029192110', 'host', 55], ['20181029192120', 'host', 60],
                ['20181029192130', 'host', 65], ['20181029192140', 'host', 70], ['20181029192150', 'host', 75],
                ['20181029192200', 'host', 80], ['20181029192210', 'host', 85], ['20181029192220', 'host', 90],
                ['20181029192230', 'host', 95], ['20181029192240', 'host', 100], ['20181029192250', 'host', 105],
                ['20181029192300', 'host', 110], ['20181029192310', 'host', 115], ['20181029192320', 'host', 120],
                ['20181029192330', 'host', 125], ['20181029192340', 'host', 130], ['20181029192350', 'host', 135],
                ['20181029192400', 'host', 140], ['20181029192410', 'host', 145], ['20181029192420', 'host', 150],
                ['20181029192430', 'host', 155], ['20181029192440', 'host', 160], ['20181029192450', 'host', 165],
                ]

        cls.test_df = forecastsTests.sqlCtx.createDataFrame(data,['time','host','value'])
        cls.test_df2 = forecastsTests.sqlCtx.read.format('csv') \
                                               .option("header", "true") \
                                               .option("inferschema", "true") \
                                               .load("plaform2_DATE_CNT.csv")

    def command_excute(self, cond):
        command = forecastsCommand()
        parsed_args = command.parse(cond)
        df = command.execute(forecastsTests.sqlCtx, self.test_df, parsed_args)
        return df.collect()

    def command_excute2(self, cond):
        command = forecastsCommand()
        parsed_args = command.parse(cond)
        df = command.execute(forecastsTests.sqlCtx, self.test_df2, parsed_args)
        return df.collect()

    def test_case1(self):
        rows = []
        result = self.command_excute2("DATETIME_10M CNT alg=seasonal seasonality=monthly deviations=1")
        for i in range(len(result)) :
            rows.append([result[i]['DATETIME_10M'],result[i]['CNT'],result[i]['forecasts']])
        answer = [[u'2018-11-02 08:00:00', 1355.0, False], [u'2018-11-02 08:10:00', 1417.0, False], [u'2018-11-02 08:20:00', 1388.0, False], [u'2018-11-02 08:30:00', 1418.0, False],
                  [u'2018-11-02 08:40:00', 1441.0, False], [u'2018-11-02 08:50:00', 1418.0, False], [u'2018-11-02 09:00:00', 1412.0, False], [u'2018-11-02 09:10:00', 1428.0, False],
                  [u'2018-11-02 09:20:00', 1418.0, False], [u'2018-11-02 09:30:00', 1388.0, False], [u'2018-11-02 09:40:00', 1418.0, False], [u'2018-11-02 09:50:00', 1441.0, False],
                  [u'2018-11-02 10:00:00', 1412.0, False], [u'2018-11-02 10:10:00', 1418.0, False], [u'2018-11-02 10:20:00', 1417.0, False], [u'2018-11-02 10:30:00', 1388.0, False],
                  [u'2018-11-02 10:40:00', 1418.0, False], [u'2018-11-02 10:50:00', 1417.0, False], [u'2018-11-02 11:00:00', 1437.0, False], [u'2018-11-02 11:10:00', 1417.0, False],
                  [u'2018-11-02 11:20:00', 1418.0, False], [u'2018-11-02 11:30:00', 1389.0, False], [u'2018-11-02 11:40:00', 1417.0, False], [u'2018-11-02 11:50:00', 1418.0, False],
                  [u'2018-11-02 12:00:00', 1412.0, False], [u'2018-11-02 12:10:00', 1442.0, False], [u'2018-11-02 12:20:00', 1419.0, False], [u'2018-11-02 12:30:00', 1388.0, False],
                  [u'2018-11-02 12:40:00', 1417.0, False], [u'2018-11-02 12:50:00', 1418.0, False], [u'2018-11-02 13:00:00', 1412.0, False], [u'2018-11-02 13:10:00', 1418.0, False],
                  [u'2018-11-02 13:20:00', 1441.0, False], [u'2018-11-02 13:30:00', 1388.0, False], [u'2018-11-02 13:40:00', 1418.0, False], [u'2018-11-02 13:50:00', 1417.0, False],
                  [u'2018-11-02 14:00:00', 1412.0, False], [u'2018-11-02 14:10:00', 1418.0, False], [u'2018-11-02 14:20:00', 1417.0, False], [u'2018-11-02 14:30:00', 1413.0, False],
                  [u'2018-11-02 14:40:00', 1417.0, False], [u'2018-11-02 14:50:00', 1417.0, False], [u'2018-11-02 15:00:00', 1413.0, False], [u'2018-11-02 15:10:00', 1417.0, False],
                  [u'2018-11-02 15:20:00', 1418.0, False], [u'2018-11-02 15:30:00', 1388.0, False], [u'2018-11-02 15:40:00', 1441.0, False], [u'2018-11-02 15:50:00', 1418.0, False],
                  [u'2018-11-02 16:00:00', 1412.0, False], [u'2018-11-02 16:10:00', 1417.0, False], [u'2018-11-02 16:20:00', 1418.0, False], [u'2018-11-02 16:30:00', 1388.0, False],
                  [u'2018-11-02 16:40:00', 1418.0, False], [u'2018-11-02 16:50:00', 1446.0, False], [u'2018-11-02 17:00:00', 1430.0, False], [u'2018-11-02 17:10:00', 1418.0, False],
                  [u'2018-11-02 17:20:00', 1425.0, False], [u'2018-11-02 17:30:00', 1400.0, False], [u'2018-11-02 17:40:00', 1417.0, False], [u'2018-11-02 17:50:00', 1419.0, False],
                  [u'2018-11-02 18:00:00', 1437.0, False], [u'2018-11-02 18:10:00', 1418.0, False], [u'2018-11-02 18:20:00', 1417.0, False], [u'2018-11-02 18:30:00', 1389.0, False],
                  [u'2018-11-02 18:40:00', 1417.0, False], [u'2018-11-02 18:50:00', 1418.0, False], [u'2018-11-02 19:00:00', 1412.0, False], [u'2018-11-02 19:10:00', 1443.0, False],
                  [u'2018-11-02 19:20:00', 1418.0, False], [u'2018-11-02 19:30:00', 1388.0, False], [u'2018-11-02 19:40:00', 1418.0, False], [u'2018-11-02 19:50:00', 1417.0, False],
                  [u'2018-11-02 20:00:00', 1412.0, False], [u'2018-11-02 20:10:00', 1418.0, False], [u'2018-11-02 20:20:00', 1441.0, False], [u'2018-11-02 20:30:00', 1388.0, False],
                  [u'2018-11-02 20:40:00', 1418.0, False], [u'2018-11-02 20:50:00', 1417.0, False], [u'2018-11-02 21:00:00', 1413.0, False], [u'2018-11-02 21:10:00', 1417.0, False],
                  [u'2018-11-02 21:20:00', 1417.0, False], [u'2018-11-02 21:30:00', 1413.0, False], [u'2018-11-02 21:40:00', 1417.0, False], [u'2018-11-02 21:50:00', 1418.0, False],
                  [u'2018-11-02 22:00:00', 1412.0, False], [u'2018-11-02 22:10:00', 1417.0, False], [u'2018-11-02 22:20:00', 1420.0, False], [u'2018-11-02 22:30:00', 1388.0, False],
                  [u'2018-11-02 22:40:00', 1441.0, False], [u'2018-11-02 22:50:00', 1418.0, False], [u'2018-11-02 23:00:00', 1412.0, False], [u'2018-11-02 23:10:00', 1418.0, False],
                  [u'2018-11-02 23:20:00', 1417.0, False], [u'2018-11-02 23:30:00', 1388.0, False], [u'2018-11-02 23:40:00', 1418.0, False], [u'2018-11-02 23:50:00', 1448.0, False],
                  [u'2018-11-03 00:00:00', 1414.0, False], [u'2018-11-03 00:10:00', 1418.0, False], [u'2018-11-03 00:20:00', 1417.0, False], [u'2018-11-03 00:30:00', 1389.0, False],
                  [u'2018-11-03 00:40:00', 1417.0, False], [u'2018-11-03 00:50:00', 1417.0, False], [u'2018-11-03 01:00:00', 1509.0, False], [u'2018-11-03 01:10:00', 1487.0, False],
                  [u'2018-11-03 01:20:00', 1488.0, False], [u'2018-11-03 01:30:00', 1458.0, False], [u'2018-11-03 01:40:00', 1487.0, False], [u'2018-11-03 01:50:00', 1488.0, False],
                  [u'2018-11-03 02:00:00', 1414.0, False], [u'2018-11-03 02:10:00', 1435.0, False], [u'2018-11-03 02:20:00', 1424.0, False], [u'2018-11-03 02:30:00', 1388.0, False],
                  [u'2018-11-03 02:40:00', 1418.0, False], [u'2018-11-03 02:50:00', 1417.0, False], [u'2018-11-03 03:00:00', 1413.0, False], [u'2018-11-03 03:10:00', 1426.0, False],
                  [u'2018-11-03 03:20:00', 1435.0, False], [u'2018-11-03 03:30:00', 1394.0, False], [u'2018-11-03 03:40:00', 1418.0, False], [u'2018-11-03 03:50:00', 1417.0, False],
                  [u'2018-11-03 04:00:00', 1414.0, False], [u'2018-11-03 04:10:00', 1417.0, False], [u'2018-11-03 04:20:00', 1417.0, False], [u'2018-11-03 04:30:00', 1407.0, False],
                  [u'2018-11-03 04:40:00', 1423.0, False], [u'2018-11-03 04:50:00', 1418.0, False], [u'2018-11-03 05:00:00', 1412.0, False], [u'2018-11-03 05:10:00', 1417.0, False],
                  [u'2018-11-03 05:20:00', 1418.0, False], [u'2018-11-03 05:30:00', 1388.0, False], [u'2018-11-03 05:40:00', 1417.0, False], [u'2018-11-03 05:50:00', 1442.0, False],
                  [u'2018-11-03 06:00:00', 1412.0, False], [u'2018-11-03 06:10:00', 1418.0, False], [u'2018-11-03 06:20:00', 1417.0, False], [u'2018-11-03 06:30:00', 1388.0, False],
                  [u'2018-11-03 06:40:00', 1418.0, False], [u'2018-11-03 06:50:00', 1417.0, False], [u'2018-11-03 07:00:00', 1436.0, False], [u'2018-11-03 07:10:00', 1418.0, False],
                  [u'2018-11-03 07:20:00', 1417.0, False], [u'2018-11-03 07:30:00', 1418.0, False], [u'2018-11-03 07:40:00', 1388.0, False], [u'2018-11-03 07:50:00', 1417.0, False],
                  [u'2018-11-03 08:00:00', 1442.0, False], [u'2018-11-03 08:10:00', 1412.0, False], [u'2018-11-03 08:20:00', 1418.0, False], [u'2018-11-03 08:30:00', 1417.0, False],
                  [u'2018-11-03 08:40:00', 1388.0, False], [u'2018-11-03 08:50:00', 1418.0, False], [u'2018-11-03 09:00:00', 1441.0, False], [u'2018-11-03 09:10:00', 1388.0, False],
                  [u'2018-11-03 09:20:00', 1443.0, False], [u'2018-11-03 09:30:00', 1417.0, False], [u'2018-11-03 09:40:00', 1431.13, True], [u'2018-11-03 09:50:00', 1444.34, True],
                  [u'2018-11-03 10:00:00', 1432.18, True], [u'2018-11-03 10:10:00', 1431.74, True], [u'2018-11-03 10:20:00', 1431.89, True], [u'2018-11-03 10:30:00', 1411.29, True],
                  [u'2018-11-03 10:40:00', 1426.78, True], [u'2018-11-03 10:50:00', 1431.39, True], [u'2018-11-03 11:00:00', 1444.93, True], [u'2018-11-03 11:10:00', 1431.88, True],
                  [u'2018-11-03 11:20:00', 1444.53, True], [u'2018-11-03 11:30:00', 1420.82, True], [u'2018-11-03 11:40:00', 1434.58, True], [u'2018-11-03 11:50:00', 1447.93, True],
                  [u'2018-11-03 12:00:00', 1436.08, True], [u'2018-11-03 12:10:00', 1435.38, True], [u'2018-11-03 12:20:00', 1435.58, True], [u'2018-11-03 12:30:00', 1415.16, True],
                  [u'2018-11-03 12:40:00', 1430.27, True], [u'2018-11-03 12:50:00', 1435.09, True], [u'2018-11-03 13:00:00', 1448.71, True], [u'2018-11-03 13:10:00', 1435.33, True],
                  [u'2018-11-03 13:20:00', 1448.33, True], [u'2018-11-03 13:30:00', 1424.61, True], [u'2018-11-03 13:40:00', 1438.37, True], [u'2018-11-03 13:50:00', 1451.71, True],
                  [u'2018-11-03 14:00:00', 1439.86, True], [u'2018-11-03 14:10:00', 1439.17, True], [u'2018-11-03 14:20:00', 1439.37, True], [u'2018-11-03 14:30:00', 1418.94, True],
                  [u'2018-11-03 14:40:00', 1434.05, True], [u'2018-11-03 14:50:00', 1438.88, True], [u'2018-11-03 15:00:00', 1452.5, True], [u'2018-11-03 15:10:00', 1439.11, True],
                  [u'2018-11-03 15:20:00', 1452.12, True], [u'2018-11-03 15:30:00', 1428.39, True], [u'2018-11-03 15:40:00', 1442.15, True], [u'2018-11-03 15:50:00', 1455.49, True],
                  [u'2018-11-03 16:00:00', 1443.65, True], [u'2018-11-03 16:10:00', 1442.95, True], [u'2018-11-03 16:20:00', 1443.15, True], [u'2018-11-03 16:30:00', 1422.72, True],
                  [u'2018-11-03 16:40:00', 1437.83, True], [u'2018-11-03 16:50:00', 1442.66, True], [u'2018-11-03 17:00:00', 1456.28, True], [u'2018-11-03 17:10:00', 1442.89, True],
                  [u'2018-11-03 17:20:00', 1455.9, True], [u'2018-11-03 17:30:00', 1432.17, True], [u'2018-11-03 17:40:00', 1445.93, True], [u'2018-11-03 17:50:00', 1459.28, True],
                  [u'2018-11-03 18:00:00', 1447.43, True], [u'2018-11-03 18:10:00', 1446.73, True], [u'2018-11-03 18:20:00', 1446.93, True], [u'2018-11-03 18:30:00', 1426.51, True],
                  [u'2018-11-03 18:40:00', 1441.62, True], [u'2018-11-03 18:50:00', 1446.44, True], [u'2018-11-03 19:00:00', 1460.06, True], [u'2018-11-03 19:10:00', 1446.68, True],
                  [u'2018-11-03 19:20:00', 1459.68, True], [u'2018-11-03 19:30:00', 1435.95, True], [u'2018-11-03 19:40:00', 1449.71, True], [u'2018-11-03 19:50:00', 1463.06, True],
                  [u'2018-11-03 20:00:00', 1451.21, True], [u'2018-11-03 20:10:00', 1450.52, True], [u'2018-11-03 20:20:00', 1450.71, True], [u'2018-11-03 20:30:00', 1430.29, True],
                  [u'2018-11-03 20:40:00', 1445.4, True], [u'2018-11-03 20:50:00', 1450.22, True], [u'2018-11-03 21:00:00', 1463.84, True], [u'2018-11-03 21:10:00', 1450.46, True],
                  [u'2018-11-03 21:20:00', 1463.46, True], [u'2018-11-03 21:30:00', 1439.74, True], [u'2018-11-03 21:40:00', 1453.5, True], [u'2018-11-03 21:50:00', 1466.84, True],
                  [u'2018-11-03 22:00:00', 1454.99, True], [u'2018-11-03 22:10:00', 1454.3, True], [u'2018-11-03 22:20:00', 1454.5, True], [u'2018-11-03 22:30:00', 1434.07, True],
                  [u'2018-11-03 22:40:00', 1449.18, True], [u'2018-11-03 22:50:00', 1454.01, True], [u'2018-11-03 23:00:00', 1467.63, True], [u'2018-11-03 23:10:00', 1454.24, True],
                  [u'2018-11-03 23:20:00', 1467.25, True], [u'2018-11-03 23:30:00', 1443.52, True], [u'2018-11-03 23:40:00', 1457.28, True], [u'2018-11-03 23:50:00', 1470.62, True],
                  [u'2018-11-04 00:00:00', 1458.78, True], [u'2018-11-04 00:10:00', 1458.08, True], [u'2018-11-04 00:20:00', 1458.28, True], [u'2018-11-04 00:30:00', 1437.85, True],
                  [u'2018-11-04 00:40:00', 1452.96, True], [u'2018-11-04 00:50:00', 1457.79, True], [u'2018-11-04 01:00:00', 1471.41, True], [u'2018-11-04 01:10:00', 1458.02, True],
                  [u'2018-11-04 01:20:00', 1471.03, True], [u'2018-11-04 01:30:00', 1447.3, True], [u'2018-11-04 01:40:00', 1461.06, True], [u'2018-11-04 01:50:00', 1474.41, True],
                  [u'2018-11-04 02:00:00', 1462.56, True], [u'2018-11-04 02:10:00', 1461.86, True], [u'2018-11-04 02:20:00', 1462.06, True], [u'2018-11-04 02:30:00', 1441.64, True],
                  [u'2018-11-04 02:40:00', 1456.75, True], [u'2018-11-04 02:50:00', 1461.57, True], [u'2018-11-04 03:00:00', 1475.19, True], [u'2018-11-04 03:10:00', 1461.81, True],
                  [u'2018-11-04 03:20:00', 1474.81, True], [u'2018-11-04 03:30:00', 1451.08, True], [u'2018-11-04 03:40:00', 1464.85, True], [u'2018-11-04 03:50:00', 1478.19, True],
                  [u'2018-11-04 04:00:00', 1466.34, True], [u'2018-11-04 04:10:00', 1465.65, True], [u'2018-11-04 04:20:00', 1465.85, True], [u'2018-11-04 04:30:00', 1445.42, True],
                  [u'2018-11-04 04:40:00', 1460.53, True], [u'2018-11-04 04:50:00', 1465.36, True], [u'2018-11-04 05:00:00', 1478.98, True], [u'2018-11-04 05:10:00', 1465.59, True],
                  [u'2018-11-04 05:20:00', 1478.6, True], [u'2018-11-04 05:30:00', 1454.87, True], [u'2018-11-04 05:40:00', 1468.63, True], [u'2018-11-04 05:50:00', 1481.97, True],
                  [u'2018-11-04 06:00:00', 1470.13, True], [u'2018-11-04 06:10:00', 1469.43, True], [u'2018-11-04 06:20:00', 1469.63, True], [u'2018-11-04 06:30:00', 1449.2, True],
                  [u'2018-11-04 06:40:00', 1464.31, True], [u'2018-11-04 06:50:00', 1469.14, True], [u'2018-11-04 07:00:00', 1482.76, True], [u'2018-11-04 07:10:00', 1469.37, True],
                  [u'2018-11-04 07:20:00', 1482.38, True], [u'2018-11-04 07:30:00', 1458.65, True], [u'2018-11-04 07:40:00', 1472.41, True], [u'2018-11-04 07:50:00', 1485.76, True],
                  [u'2018-11-04 08:00:00', 1473.91, True], [u'2018-11-04 08:10:00', 1473.21, True], [u'2018-11-04 08:20:00', 1473.41, True], [u'2018-11-04 08:30:00', 1452.98, True],
                  [u'2018-11-04 08:40:00', 1468.1, True], [u'2018-11-04 08:50:00', 1472.92, True], [u'2018-11-04 09:00:00', 1486.54, True], [u'2018-11-04 09:10:00', 1473.16, True],
                  [u'2018-11-04 09:20:00', 1486.16, True], [u'2018-11-04 09:30:00', 1462.43, True], [u'2018-11-04 09:40:00', 1476.19, True], [u'2018-11-04 09:50:00', 1489.54, True],
                  [u'2018-11-04 10:00:00', 1477.69, True], [u'2018-11-04 10:10:00', 1477.0, True], [u'2018-11-04 10:20:00', 1477.19, True], [u'2018-11-04 10:30:00', 1456.77, True],
                  [u'2018-11-04 10:40:00', 1471.88, True], [u'2018-11-04 10:50:00', 1476.7, True], [u'2018-11-04 11:00:00', 1490.32, True], [u'2018-11-04 11:10:00', 1476.94, True]]
        self.assertEqual(rows, answer)

    def test_case2(self):
        rows = []
        result = self.command_excute("time value alg=linear")
        for i in range(len(result)) :
            rows.append([result[i]['time'],result[i]['value'],result[i]['forecasts']])
        answer = [[u'2018-10-29 19:20:00', 20.0, False], [u'2018-10-29 19:20:10', 25.0, False], [u'2018-10-29 19:20:20', 30.0, False], [u'2018-10-29 19:20:30', 35.0, False],
                  [u'2018-10-29 19:20:40', 40.0, False], [u'2018-10-29 19:20:50', 45.0, False], [u'2018-10-29 19:21:00', 50.0, False], [u'2018-10-29 19:21:10', 55.0, False],
                  [u'2018-10-29 19:21:20', 60.0, False], [u'2018-10-29 19:21:30', 65.0, False], [u'2018-10-29 19:21:40', 70.0, False], [u'2018-10-29 19:21:50', 75.0, False],
                  [u'2018-10-29 19:22:00', 80.0, False], [u'2018-10-29 19:22:10', 85.0, False], [u'2018-10-29 19:22:20', 90.0, False], [u'2018-10-29 19:22:30', 95.0, False],
                  [u'2018-10-29 19:22:40', 100.0, False], [u'2018-10-29 19:22:50', 105.0, False], [u'2018-10-29 19:23:00', 110.0, False], [u'2018-10-29 19:23:10', 115.0, False],
                  [u'2018-10-29 19:23:20', 120.0, False], [u'2018-10-29 19:23:30', 125.0, False], [u'2018-10-29 19:23:40', 130.0, False], [u'2018-10-29 19:23:50', 135.0, False],
                  [u'2018-10-29 19:24:00', 140.0, False], [u'2018-10-29 19:24:10', 145.0, False], [u'2018-10-29 19:24:20', 150.0, False], [u'2018-10-29 19:24:30', 155.0, False],
                  [u'2018-10-29 19:24:40', 160.0, False], [u'2018-10-29 19:24:50', 165.0, False], [u'2018-10-29 19:25:00', 169.82133474022964, True],
                  [u'2018-10-29 19:25:10', 174.80980794927672, True], [u'2018-10-29 19:25:20', 179.7982811583238, True],
                  [u'2018-10-29 19:25:30', 184.78675436737086, True], [u'2018-10-29 19:25:40', 189.77522757641793, True],
                  [u'2018-10-29 19:25:50', 194.763700785465, True], [u'2018-10-29 19:26:00', 199.75217399451208, True],
                  [u'2018-10-29 19:26:10', 204.74064720355915, True], [u'2018-10-29 19:26:20', 209.72912041260622, True],
                  [u'2018-10-29 19:26:30', 214.7175936216533, True], [u'2018-10-29 19:26:40', 219.70606683070037, True],
                  [u'2018-10-29 19:26:50', 224.69454003974744, True], [u'2018-10-29 19:27:00', 229.6830132487945, True],
                  [u'2018-10-29 19:27:10', 234.67148645784158, True], [u'2018-10-29 19:27:20', 239.65995966688865, True],
                  [u'2018-10-29 19:27:30', 244.64843287593573, True], [u'2018-10-29 19:27:40', 249.6369060849828, True],
                  [u'2018-10-29 19:27:50', 254.62537929402987, True], [u'2018-10-29 19:28:00', 259.613852503077, True],
                  [u'2018-10-29 19:28:10', 264.60232571212407, True], [u'2018-10-29 19:28:20', 269.59079892117114, True],
                  [u'2018-10-29 19:28:30', 274.5792721302182, True], [u'2018-10-29 19:28:40', 279.5677453392653, True],
                  [u'2018-10-29 19:28:50', 284.55621854831236, True], [u'2018-10-29 19:29:00', 289.54469175735943, True],
                  [u'2018-10-29 19:29:10', 294.5331649664065, True], [u'2018-10-29 19:29:20', 299.5216381754536, True],
                  [u'2018-10-29 19:29:30', 304.51011138450065, True], [u'2018-10-29 19:29:40', 309.4985845935477, True],
                  [u'2018-10-29 19:29:50', 314.4870578025948, True]]
        self.assertEqual(rows, answer)