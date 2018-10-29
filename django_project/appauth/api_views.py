from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate, login, logout

from utils.response_handler import generic_response

from appauth.api_authentications import (
    CsrfExemptSessionAuthentication,
    SessionAuthenticationUnsafeMethods,
)

from appauth.serializers import (
    AppUserSerializer,
    AppUserLoginSerializer,
)

from appauth.constants import (
    FailMessages,
    ResponseKeys,
)


class LoginAPI(GenericAPIView):
    serializer_class = AppUserLoginSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, )

    def post(self, request):
        """
        # API through which a user can login.

        Logs a user in. Creates a session and sends back the session token along with user data.
        This token is expected for all authenticated APIs.

        **Header**:

            {
                "Content-Type": "application/json"
            }
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password'])
            if user:
                if user.is_active:
                    login(request, user)
                    request.session.save()
                    user_serializer = AppUserSerializer(user)
                    context = {
                        ResponseKeys.SESSION_ID: request.session.session_key,
                        ResponseKeys.USER: user_serializer.data}
                    return Response(
                        context,
                        status=status.HTTP_200_OK)
                else:
                    return Response(
                        generic_response(FailMessages.USER_INACTIVE),
                        status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(
                    generic_response(FailMessages.INVALID_CREDENTIALS),
                    status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                generic_response(FailMessages.INVALID_CREDENTIALS),
                status=status.HTTP_400_BAD_REQUEST)


class LogoutAPI(APIView):
    authentication_classes = (SessionAuthenticationUnsafeMethods, )

    def post(self, request):
        """
        # API through which a user can logout.

        Logs a user out. Destroys the session.

        **Header**:

            {
                "Content-Type": "application/json",
                "sessionid": "token"
            }
        """
        logout(request)
        context = {
            ResponseKeys.LOGGED_OUT: True}
        return Response(
            context,
            status=status.HTTP_200_OK)


class TestAPI(APIView):
    authentication_classes = (SessionAuthenticationUnsafeMethods, )

    def post(self, request):
        """
        # An API to test auth layer

        **Header**:

            {
                "Content-Type": "application/json",
                "sessionid": "token"
            }
        """
        return Response(
            {'foo': 'bar'},
            status=status.HTTP_200_OK)
