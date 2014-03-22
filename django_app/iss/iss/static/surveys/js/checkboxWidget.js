iss.lib.widgets.CheckboxWidget = function(options) {
    return iss.lib.widgets.Widget("checkbox", options);
}

$.widget("iss.checkboxWidget", $.iss.widget, {
    options: {
        name: '',
        data: function() { return [] },
        horizontal: function() {return false },
        required: function() {return false }
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
            var checkbox = data[i]();
            $('<label ' + (this.options.horizontal() ? 
                    '' : 'style="display:block;"') + '>'
                + '<input type="checkbox" name="'
                + this.options.name() + '" id="'
                + checkbox['id']() + '" '
                + (checkbox['checked']() ? 'checked' : '')
                + '>' + checkbox['text']() + '</label>')
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

