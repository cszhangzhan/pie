'use strict'

app = angular.module('controllers', ['eventService', 'stockService'])

app.controller 'DashboardCtrl',
  class DashboardCtrl
    @$inject: ['$scope', '$interval', '$http', 'EventService', 'StockService'] 

    constructor: (@scope, @interval, @http, @EventService, @StockService) ->
      angular.extend @scope,
        eventClick: @eventClick
        eventsBeforeNow: @eventsBeforeNow
        linkBeforeNow: @linkBeforeNow
        getChartData: @getChartData
        affectsMcDonalds: @affectsMcDonalds
        affectsStarbucks: @affectsStarbucks
        reset: @reset
        timeDiff: @timeDiff

      @init()
      # @interval @init, 5000

    init: () =>
      @EventService.query().then (data) =>
        @scope.events = data.nodes
        @scope.links = data.links

        for link in @scope.links
          link.source = @scope.events.indexOf(@scope.events.findWhere(id: link.source))
          link.target = @scope.events.indexOf(@scope.events.findWhere(id: link.target))

        for node in @scope.events
          node.timestamp = new Date node.timestamp

        @eventsBeforeNow()
        @linksBeforeNow()

      @EventService.calculate().then (data) =>
        @scope.mcProb = 1 - data["6"][0]
        @scope.sbProb = 1 - data["4"][0]

    eventsBeforeNow: () =>
      @scope.filteredEvents = @scope.events.filter (event) ->
        return event.timestamp.getTime() <= new Date().getTime()

    linksBeforeNow: () =>
      @scope.filteredLinks = @scope.links.filter (link) =>
        if link.target >= @scope.filteredEvents.length or link.source >= @scope.filteredEvents.length
          return false

        true

    eventClick: (event) =>
      for item in @scope.events
        item.selected = false
      event.selected = true
      @StockService.twitter().then (data) =>
        @scope.tweets = data
      @scope.isModalOpen = true

    getChartData: () =>
      @StockService.query()

    affectsMcDonalds: (event) =>
      event.id != 4

    affectsStarbucks: (event) =>
      event.id == 1 or event.id == 2

    reset: =>
      @EventService.reset()

    update: =>
      @init()

    timeDiff: (sb) =>
      if @scope.events
        toFind = if sb then 4 else 6
        ms = @scope.events.findWhere(id: toFind).timestamp.getTime() - new Date().getTime()
        sec = Math.round((ms)/1000)
        return sec
      
