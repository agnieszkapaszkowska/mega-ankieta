$.widget("iss.imgWidget", $.iss.widget, {
    options: {
        questionWidget: null,
        condition: null,
        src: function() { return '' }
    },

    _create: function() {
        this._super();
    },

    _setOption: function(key, value) {
        if (key == "src")
            this._setText(value);
        this._super(key, value);
    },

    _setText: function(dataFun) {
        this.element.empty();
        $("<img src='" + this.options.src() + "'/>").appendTo(this.element);
    }
});
