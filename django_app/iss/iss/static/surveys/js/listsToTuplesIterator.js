iss.lib.iterators.ListsToTuplesIterator = function(options) {
    var tuple = options.data();
    var list = [];
    var minLength = -1;
    
    $.each(tuple, function(key, value) {
        var arg = value();
        if (minLength == -1 || arg.length < minLength)
            minLength = arg.length;
        list.push(arg);
    });

    var result = [];
    for (var i = 0; i < minLength; i++) {
        result.push((function(index) {
            return function() {
                var newTuple = {};
                for (var j = 0; j < list.length; j++)
                    newTuple[j] = list[j][index];
                return newTuple;
            }
        })(i));
    }

    return result;
}
