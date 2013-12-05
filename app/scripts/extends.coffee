Array::find = (fun) ->
  i = 0
  l = @length

  while i < l
    item = this[i]
    return item  if fun(item)
    ++i
  null

unless Array::filter
  Array::filter = (fun) -> #, thisp
    "use strict"
    throw new TypeError()  unless this?
    t = Object(this)
    len = t.length >>> 0
    res = undefined
    thisp = undefined
    i = undefined
    val = undefined
    throw new TypeError()  if typeof fun isnt "function"
    res = []
    thisp = arguments_[1]
    i = 0
    while i < len
      if i of t
        val = t[i] # in case fun mutates this
        res.push val  if fun.call(thisp, val, i, t)
      i++
    res

Array::where = (attrs, first) ->
  return (if first then undefined else [])  if not this? or @length is 0
  this[(if first then "find" else "filter")] (value) ->
    for key of attrs
      return false  if attrs[key] isnt value[key]
    true


Array::findWhere = (attrs) ->
  @where attrs, true