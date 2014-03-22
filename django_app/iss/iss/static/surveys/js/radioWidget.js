iss.lib.widgets.RadioWidget = function(options) {
    return iss.lib.widgets.Widget("radio", options);
}

$.widget("iss.radioWidget", $.iss.widget, {
    options: {
        name: '',
        data: function() { return [] },
        checkedIndex: function() { return -1 },
        horizontal: function() {return false },
        required: function() {return true }
    },

    _create: function() {
        this._super();
    },

    _setOption: function(key, value) {
        if (key == "data")
            this._setData(value);
        this._super(key, value);
    },

    _setData: function(dataFun) {
        this.element.find("label").remove();
        var data = dataFun();
        for (var i = 0; i < data.length; i++) {
            var radio = data[i]();
            $('<label ' + (this.options.horizontal() ? 
                    '' : 'style="display:block;"') + '>'
                + '<input type="radio" name="'
                + this.options.name() + '" id="'
                + radio['id']() + '" '
                + (i == this.options.checkedIndex() ? 'checked' : '')
                + '>' + radio['text']() + '</label>')
                .appendTo(this.element);
        }
    },
    
    validate: function() {
        if (this.options.required()
            && $('input:checked[name='
                 + this.options.name() + ']').length == 0) {
            this.element.addClass('erorr');
            return false;
        }
        return true;
    },
    
});

