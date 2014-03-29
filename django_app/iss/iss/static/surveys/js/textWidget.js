$.widget("iss.textWidget", $.iss.widget, {
    options: {
        pageWidget: null,
        condition: null,
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
