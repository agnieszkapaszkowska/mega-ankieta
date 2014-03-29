$.widget("iss.selectboxWidget", $.iss.widget, {
    options: {
        questionWidget: null,
        condition: null,
        name: '',
        data: function() { return [] },
        selectedIndex: function() { return -1 },
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

    _setCallback: function(varName) {
        var element = this.element;
        iss.vars[varName] = element.find('select')[0].selectedIndex;
        var questionWidget = this.options.questionWidget;
        element.find('select').change(
            function() {
                iss.vars[varName] = element.find('select')[0].selectedIndex;
                questionWidget.childChanged();
            });
    },
    
    validate: function() {
        if (this.options.required()
            && this.element.is(":visible")
            && this.element.find('select')[0].selectedIndex == -1) {
            this.element.addClass('erorr');
            return false;
        }
        return true;
    },
    
});

