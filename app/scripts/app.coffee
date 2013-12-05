'use strict'

app = angular.module('app', [
  'ngAnimate',
  'ngCookies',
  'ngResource',
  'ngSanitize',
  'ngRoute',
  'controllers',
  'directives'
])

app.config ($routeProvider) ->
  $routeProvider
    .when '/',
      templateUrl: 'views/dashboard/show.html'
      controller: 'DashboardCtrl'
    .otherwise
      redirectTo: '/'
