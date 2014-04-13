iss.lib.widgets.Widget = function(name, options) {
    return function(condition) {
        return function(container, questionWidget) {
                if (condition())
                    return eval("$('<div></div>')"
                        + ".appendTo(container)."
                        + name + "Widget(options, "
                        + "{'questionWidget': questionWidget, 'condition': condition})"
                        + ".data('iss-' + name + '-widget')");
                return null;
               }
           }
}

$.widget("iss.widget", {
    options: {
        condition: null,
    },

    _create: function() {
        this.element.addClass(this.widgetName);
        this.containsSubmitData = true;
        this._setOptions(this.options);
    },

    validate: function() {
        return true;
    },

    checkCondition: function() {
        if (this.options.condition != null) {
            this.containsSubmitData = this.options.condition();
            if (this.options.condition())
                this._show(this.element, this.options.show, function(){});
            else
                this._hide(this.element, this.options.hide, function(){});
        }
    },

    insertSubmitData: function(submitData) {
    },

    updateTupleArgs: function(tuple, args) {
        var i = 0;
        $.each(args, function(key, value) {
            if (tuple[key] == undefined) {
                if (tuple[i] != undefined)
                    tuple[key] = tuple[i];
                else
                    tuple[key] = value;    
                i++;
            }
        });
    }

});

