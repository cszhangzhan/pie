app = angular.module("eventModel", [])

app.factory "Event", ->
  Event = (data) ->
    
    #set defaults properties and functions
    angular.extend this,
      id: null

    angular.extend this, data

  Event