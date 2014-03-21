iss.lib.widgets.TextWidget = function(options) {
    return function(condition) {
        return function(container) {
                if (condition())
                    return $('<div></div>')
                        .appendTo(container)
                        .textWidget(options)
                        .data('iss-text-widget');
                return null;
               }
           }
}

$.widget("iss.textWidget", {
    options: {
        text: function() { return '' }
    },

    _create: function() {
        this.element.addClass('text-widget');
        this._setOptions(this.options);
    },

    _setOption: function(key, value) {
        if (key == "text")
            this._setText(value);
        this._super(key, value);
    },

    _setText: function(dataFun) {
        this.element.text(dataFun());
    }
});
