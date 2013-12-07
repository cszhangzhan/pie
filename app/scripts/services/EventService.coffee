app = angular.module("eventService", ["eventModel"])

app.factory "EventService", ($http, $q, Event) ->
  @query = () ->
    url = "http://localhost:8000/graph/get_graph"
    $http.get(url).then (response) ->
      for item in response.data.nodes
        item = new Event item

      response.data
    , (response) ->
      $q.reject response.data.error

  @calculate = () ->
    url = "http://localhost:8000/graph/get_prob"
    $http.post(url, [4, 6]).then (response) ->
      response.data
    , (response) ->
      $q.reject response.data.error

  @reset = () ->
    url = "http://localhost:8000/graph/set_topnews_time"
    $http.post(url, 2: -300).then (response) ->
      response.data
    , (response) ->
      $q.reject response.data.error

  this
