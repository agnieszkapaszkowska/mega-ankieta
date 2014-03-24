iss.lib.widgets.RadioWidget = function(options) {
    return iss.lib.widgets.Widget("radio", options);
}

$.widget("iss.radioWidget", $.iss.widget, {
    options: {
        pageWidget: null,
        condition: null,
        name: '',
        data: function() { return [] },
        checkedIndex: function() { return -1 },
        horizontal: function() {return false },
        required: function() {return true },
        resultVarName: null
    },

    _create: function() {
        this._super();
    },

    _setOption: function(key, value) {
        if (key == "data")
            this._setData(value);
        if (key == "resultVarName" && value != null)
            this._setCallback(value);
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

    _setCallback: function(varName) {
        iss.vars[varName] = this.options.checkedIndex();
        var element = this.element;
        var pageWidget = this.options.pageWidget;
        element.find('input').click(
            function() {
                iss.vars[varName] = element.find('input')
                            .index(element.find('input:checked'));
                pageWidget.childChanged();
            });
    },
    
    validate: function() {
        if (this.options.required()
            && this.element.find('input:checked').length == 0) {
            this.element.addClass('erorr');
            return false;
        }
        return true;
    },
    
});

