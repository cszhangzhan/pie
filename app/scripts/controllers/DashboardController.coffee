'use strict'

app = angular.module 'controllers', []

app.controller 'DashboardCtrl',
  class DashboardCtrl
    @$inject: ['$scope'] 

    constructor: (@scope) ->
      angular.extend @scope,
        eventClick: @eventClick

      @scope.topNewsIds = [2, 3]
      @scope.events =
        [
          timestamp: 1386111201.270364
          isResult: false
          id: 1
          title: "nil"
        ,
          timestamp: 1386111206.270364
          isResult: false
          id: 2
          title: "nil"
        ,
          timestamp: 1386111206.270364
          isResult: false
          id: 3
          title: "nil"
        ,
          timestamp: 1386111216.270364
          isResult: true
          id: 4
          title: "nil"
        ,
          timestamp: 1386111211.270364
          isResult: false
          id: 5
          title: "nil"
        ,
          timestamp: 1386111216.270364
          isResult: true
          id: 6
          title: "nil"
        ]

      @scope.links =
        [
          source: 1
          target: 2
          propagation: 5
        ,
          source: 1
          target: 3
          propagation: 5
        ,
          source: 2
          target: 4
          propagation: 10
        ,
          source: 2
          target: 6
          propagation: 10
        ,
          source: 3
          target: 5
          propagation: 5
        ,
          source: 5
          target: 6
          propagation: 5
        ]

      for link in @scope.links
        link.source = @scope.events.indexOf(@scope.events.findWhere(id: link.source))
        link.target = @scope.events.indexOf(@scope.events.findWhere(id: link.target))

      for node in @scope.events
        node.timestamp = new Date node.timestamp
        node.topNews = if @scope.topNewsIds.indexOf(node.id) != -1 then true else false


    eventClick: (event) =>
      for item in @scope.events
        item.selected = false
      event.selected = true
      @scope.isModalOpen = true
