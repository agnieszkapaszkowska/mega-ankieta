iss.lib.iterators.SubsetIterator = function(options) {
    var list = options.data();
    return shuffle(list).slice(0, options.number());
}
