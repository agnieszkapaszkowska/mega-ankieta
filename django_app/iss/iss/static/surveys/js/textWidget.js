iss.lib.widgets.TextWidget = function(options) {
    return iss.lib.widgets.Widget("text", options);
}

$.widget("iss.textWidget", $.iss.widget, {
    options: {
        text: function() { return '' }
    },

    _create: function() {
        this._super();
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
