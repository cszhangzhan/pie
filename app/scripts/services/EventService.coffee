app = angular.module("eventService", ["eventModel"])

app.factory "EventService", ($http, $q, Event) ->
  @query = () ->
    url = "/graph/get_graph"
    $http.get(url).then (response) ->
      new Event response.data
    , (response) ->
      $q.reject response.data.error

  this
