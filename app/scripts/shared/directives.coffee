app = angular.module('directives', [])
directives = {}

directives.graph = ($parse, $timeout) ->
  restrict: "E"
  replace: false
  scope:
    nodes: "&graphNodes"
    links: "&graphLinks"

  link: (scope, element, attrs) ->
    do start = ->
      if not scope.nodes()
        $timeout start, 1000
      else
        nodeData = scope.nodes()
        linkData = scope.links()

        container = d3.select(element[0])

        width = element.width()
        height = element.height()

        color = d3.scale.category20c()
        force = d3.layout.force().charge(-500).linkDistance(90).size([550, 350])
        svg = container.append("svg").attr("preserveAspectRatio", "xMinYMin meet").attr("viewBox", "0 0 550 350")

        svg.append("svg:defs").append("svg:marker")
        .attr("id", "arrowhead")
        .attr("refX", 9)
        .attr("refY", 2)
        .attr("markerWidth", 8)
        .attr("markerHeight", 4)
        .attr("orient", "auto")
        .append("path")
        .attr("d", "M 0,0 V 4 L6,2 Z")

        svg.append("svg:defs").append("svg:marker")
        .attr("id", "arrowhead-active")
        .attr("refX", 9)
        .attr("refY", 2)
        .attr("markerWidth", 8)
        .attr("markerHeight", 4)
        .attr("orient", "auto")
        .append("path")
        .attr("d", "M 0,0 V 4 L6,2 Z")
        .attr("fill", "red")

        force.nodes(nodeData).links(linkData).start()
        link = svg.selectAll(".link").data(linkData).enter().append("line").attr("class", "link").attr("marker-end", "url(#arrowhead)")

        node = svg.selectAll(".node").data(nodeData).enter().append("g").attr("class", "node").call(force.drag)

        label = node.append("g")

        text = label.append("text")
          .attr("dx", 12)
          .attr("dy", ".35em")
          .attr("fill", "black")
          .text (d) ->
            return d.title.substring(0,15) + "..."

        circle = node.append("circle")
          .attr("r", 7)
          .attr("x", -8)
          .attr("y", -8)

        scope.$watch -> 
          circle.attr "fill", (d) ->
            if d.selected
              "red"
            else
              if d.isResult
                "green"
              else
                "black"

          targets = new Array
          link.classed("active", (d) ->
            if d.source.selected
              targets.push d.target.id
              true
            else if targets.indexOf(d.source.id) != -1
              true)
          .attr("marker-end", (d) ->
            if d.source.selected
              "url(#arrowhead-active)"
            else if targets.indexOf(d.source.id) != -1
              "url(#arrowhead-active)"
            else
              "url(#arrowhead)")
        , true

        force.on "tick", ->
          link.attr("x1", (d) ->
            d.source.x
          ).attr("y1", (d) ->
            d.source.y
          ).attr("x2", (d) ->
            d.target.x
          ).attr "y2", (d) ->
            d.target.y

          node.attr("transform", (d) ->
            "translate(" + d.x + "," + d.y + ")"
          ).attr("style")

directives.map = ($parse, $timeout) ->
  restrict: "C"
  replace: false
  scope:
    data: "=markerData"
  link: (scope, element, attrs) ->
    map = L.mapbox.map(element[0], "pfacheris.gf8171eo").setView([37.8, -96], 4)

    do start = ->
      if not scope.data
        $timeout start, 1000
      else
        for marker in scope.data
          L.mapbox.markerLayer(
            type: "Feature"
            geometry:
              type: "Point"
              coordinates: marker.location.reverse()

            properties:
              title: ""
              description: marker.title
              "marker-size": "large"
              "marker-color": "#00D6DD"
          ).addTo map

directives.chart = ($parse) ->
  restrict: "C"
  replace: false
  scope:
    data: "&chartData"
    title: "=chartTitle"
  link: (scope, element, attrs) ->
    element.highcharts "StockChart",
      chart:
        backgroundColor: "#f8f8f8" 
        height: 325

      rangeSelector:
        selected: 1

      title:
        text: "MCD" + " Stock Price"

      series: [
        name: "MCD"
        data: scope.data()
        tooltip:
          valueDecimals: 2
      ]

app.directive directives
