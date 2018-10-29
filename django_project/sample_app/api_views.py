from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import random


class AnomaliesDetectedAPI(APIView):

    def get(self, context):
        context = {
            'mainText': random.randint(10000, 1000000),
            'subText': 'Anomalies Detected'}
        return Response(
            context,
            status=status.HTTP_200_OK)


class AccountsScannedAPI(APIView):

    def get(self, context):
        context = {
            'mainText': random.randint(10000, 1000000),
            'subText': 'Accounts Scanned'}
        return Response(
            context,
            status=status.HTTP_200_OK)


class LogsProcessedAPI(APIView):

    def get(self, context):
        context = {
            'mainText': random.randint(10000, 1000000),
            'subText': 'Logs Processed'}
        return Response(
            context,
            status=status.HTTP_200_OK)


class PeanutsEatenAPI(APIView):

    def get(self, context):
        context = {
            'mainText': random.randint(10000, 1000000),
            'subText': 'Peanuts Eaten'}
        return Response(
            context,
            status=status.HTTP_200_OK)


class YearlySalesAPI(APIView):
    """
    This is a sample API for testing charts
    """

    def get(self, request):
        """
        This is a sample API for testing charts

        **Header**:

            {
                "Content-Type": "application/json"
            }
        """
        context = {
            'label': 'Yearly Sales',
            'type': 'line',
            'data': {
                'labels': ["2012", "2013", "2014", "2015", "2016", "2017", "2018"],
                'type': 'line',
                'defaultFontFamily': 'Montserrat',
                'datasets': [
                    {
                        'label': "Foods",
                        'data': [0, 30, 15, 110, 50, 63, 120],
                        'backgroundColor': 'transparent',
                        'borderColor': 'rgba(220,53,69,0.75)',
                        'borderWidth': 3,
                        'pointStyle': 'circle',
                        'pointRadius': 5,
                        'pointBorderColor': 'transparent',
                        'pointBackgroundColor': 'rgba(220,53,69,0.75)',
                    }, {
                        'label': "Electronics",
                        'data': [0, 50, 40, 80, 35, 99, 80],
                        'backgroundColor': 'transparent',
                        'borderColor': 'rgba(40,167,69,0.75)',
                        'borderWidth': 3,
                        'pointStyle': 'circle',
                        'pointRadius': 5,
                        'pointBorderColor': 'transparent',
                        'pointBackgroundColor': 'rgba(40,167,69,0.75)'}]},
            'options': {
                'responsive': True,
                'tooltips': {
                    'mode': 'index',
                    'titleFontSize': 12,
                    'titleFontColor': '#000',
                    'bodyFontColor': '#000',
                    'backgroundColor': '#fff',
                    'titleFontFamily': 'Montserrat',
                    'bodyFontFamily': 'Montserrat',
                    'cornerRadius': 3,
                    'intersect': False},
                'legend': {
                    'display': False,
                    'labels': {
                        'usePointStyle': True,
                        'fontFamily': 'Montserrat'}},
                'scales': {
                    'xAxes': [{
                        'display': True,
                        'gridLines': {
                            'display': False,
                            'drawBorder': False
                        },
                        'scaleLabel': {
                            'display': False,
                            'labelString': 'Month'
                        }}],
                    'yAxes': [{
                        'display': True,
                        'gridLines': {
                            'display': False,
                            'drawBorder': False
                        },
                        'scaleLabel': {
                            'display': True,
                            'labelString': 'Value'
                        }}]
                },
                'title': {
                    'display': False,
                    'text': 'Normal Legend'}}
        }
        return Response(
            context,
            status=status.HTTP_200_OK)


class BarChartAPI(APIView):
    """
    This is a sample API for testing charts
    """

    def get(self, request):
        """
        This is a sample API for testing charts

        **Header**:

            {
                "Content-Type": "application/json"
            }
        """
        context = {
            'label': 'Profits',
            'type': 'bar',
            'data': {
                'labels': ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
                'datasets': [
                    {
                        'label': "My First dataset",
                        'data': [65, 59, 80, 81, 56, 55, 45],
                        'borderColor': "rgba(0, 194, 146, 0.9)",
                        'borderWidth': "0",
                        'backgroundColor': "rgba(0, 194, 146, 0.5)"
                    },
                    {
                        'label': "My Second dataset",
                        'data': [28, 48, 40, 19, 86, 27, 76],
                        'borderColor': "rgba(0,0,0,0.09)",
                        'borderWidth': "0",
                        'backgroundColor': "rgba(0,0,0,0.07)"
                    }]},
            'options': {
                'scales': {
                    'yAxes': [{
                        'ticks': {
                            'beginAtZero': True}}]}}
        }
        return Response(
            context,
            status=status.HTTP_200_OK)


class RadarChartAPI(APIView):
    """
    This is a sample API for testing charts
    """

    def get(self, request):
        """
        This is a sample API for testing charts

        **Header**:

            {
                "Content-Type": "application/json"
            }
        """
        context = {
            'label': 'Radar Chart',
            'type': 'radar',
            'data': {
                'labels': [
                    ["Eating", "Dinner"],
                    ["Drinking", "Water"],
                    "Sleeping",
                    ["Designing", "Graphics"],
                    "Coding",
                    "Cycling",
                    "Running"],
                'datasets': [
                    {
                        'label': "My First dataset",
                        'data': [65, 70, 66, 45, 5, 55, 40],
                        'borderColor': "rgba(0, 194, 146, 0.6)",
                        'borderWidth': "1",
                        'backgroundColor': "rgba(0, 194, 146, 0.4)"
                    },
                    {
                        'label': "My Second dataset",
                        'data': [28, 5, 55, 19, 63, 27, 68],
                        'borderColor': "rgba(0, 194, 146, 0.7",
                        'borderWidth': "1",
                        'backgroundColor': "rgba(0, 194, 146, 0.5)"
                    }
                ]
            },
            'options': {
                'legend': {
                    'position': 'top'
                },
                'scale': {
                    'ticks': {
                        'beginAtZero': True
                    }
                }
            }
        }
        return Response(
            context,
            status=status.HTTP_200_OK)


class DoughnutChartAPI(APIView):
    """
    This is a sample API for testing charts
    """

    def get(self, request):
        """
        This is a sample API for testing charts

        **Header**:

            {
                "Content-Type": "application/json"
            }
        """
        context = {
            'label': 'Doughnut Chart',
            'type': 'doughnut',
            'data': {
                'datasets': [{
                    'data': [35, 40, 20, 5],
                    'backgroundColor': [
                        "rgba(0, 194, 146,0.9)",
                        "rgba(0, 194, 146,0.7)",
                        "rgba(0, 194, 146,0.5)",
                        "rgba(0,0,0,0.07)"],
                    'hoverBackgroundColor': [
                        "rgba(0, 194, 146,0.9)",
                        "rgba(0, 194, 146,0.7)",
                        "rgba(0, 194, 146,0.5)",
                        "rgba(0,0,0,0.07)"]
                }],
                'labels': [
                    "green",
                    "green",
                    "green",
                    "green"]},
            'options': {
                'responsive': True}
        }
        return Response(
            context,
            status=status.HTTP_200_OK)
