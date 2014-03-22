iss.lib.widgets.TextareaWidget = function(options) {
    return iss.lib.widgets.Widget("textarea", options);
}

$.widget("iss.textareaWidget", $.iss.widget, {
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
        $('<label>' + this.options.label() + '</label><br/>')
            .appendTo(this.element);
        $('<textarea name="' + this.options.name()
            + '" placeholder="' + this.options.placeholder()
            + '"></textarea>').appendTo(this.element);
    },

    validate: function() {
        if (this.options.required()
            && $('textarea[name=' + this.options.name()
                 + ']').val().length == 0) {
            this.element.addClass("error");
            return false;
        }
        return true;
    }
});
