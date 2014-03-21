iss.lib.widgets.CheckboxWidget = function(options) {
    return function(condition) {
        return function(container) {
                if (condition())
                    return $('<div></div>')
                        .appendTo(container)
                        .checkboxWidget(options)
                        .data('iss-checkbox-widget');
                return null;
               }
           }
}

$.widget("iss.checkboxWidget", {
    options: {
        name: '',
        data: function() { return [] }
    },

    _create: function() {
        this.element.addClass('checkbox-widget');
        this._setOptions(this.options);
    },

    _setOption: function(key, value) {
        if (key == "data")
            this._setData(value);
        this._super(key, value);
    },

    _setData: function(dataFun) {
        this.element.find("div").remove();
        var data = dataFun();
        for (var i = 0; i < data.length; i++) {
            var checkbox = data[i]();
            $('<div><label><input type="checkbox" name="'
                + this.options.name() + '" id="'
                + checkbox['id']() + '" '
                + (checkbox['checked']() ? 'checked' : '')
                + '>' + checkbox['text']() + '</label><div>')
                .appendTo(this.element);
        }
    }
});

