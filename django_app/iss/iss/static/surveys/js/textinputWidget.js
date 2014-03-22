iss.lib.widgets.TextinputWidget = function(options) {
    return iss.lib.widgets.Widget("textinput", options);
}

$.widget("iss.textinputWidget", $.iss.widget, {
    options: {
        name: function() { return '' },
        label: function() { return '' },
        placeholder: function() { return '' },
        required: function() { return true }
    },

    _create: function() {
        this._super();
    },

    _setOption: function(key, value) {
        if (key == "label")
            this._setTextarea(value);
        this._super(key, value);
    },

    _setTextarea: function(dataFun) {
        $('<label>' + this.options.label() + ':</label>')
            .appendTo(this.element);
        $('<input type="text" name="' + this.options.name()
            + '" placeholder="' + this.options.placeholder()
            + '"></input>').appendTo(this.element);
    },

    validate: function() {
        if (this.options.required()
            && $('input[name=' + this.options.name()
                 + ']').val().length == 0) {
            this.element.addClass("error");
            return false;
        }
        return true;
    }
});
