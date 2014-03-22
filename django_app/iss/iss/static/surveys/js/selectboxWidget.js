iss.lib.widgets.SelectboxWidget = function(options) {
    return iss.lib.widgets.Widget("selectbox", options);
}

$.widget("iss.selectboxWidget", $.iss.widget, {
    options: {
        name: '',
        data: function() { return [] },
        selectedIndex: function() { return -1 },
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
        this.element.find("select").remove();
        var selectTag = $('<select name="' + this.options.name()
                          + '"></select>').appendTo(this.element);
        var data = dataFun();
        for (var i = 0; i < data.length; i++) {
            var option = data[i]();
            $('<option value="'
                + option['id']() + '" '
                + (i == this.options.selectedIndex() ? 'selected' : '')
                + '>' + option['text']() + '</option>')
                .appendTo(selectTag);
        }
    },
    
    validate: function() {
        if (this.options.required()
            && $('select[name='
                 + this.options.name() + ']').selectedIndex == -1) {
            this.element.addClass('erorr');
            return false;
        }
        return true;
    },
    
});

