iss.lib.widgets.Widget = function(name, options) {
    return function(condition) {
        return function(container, pageWidget) {
                if (condition())
                    return eval("$('<div></div>')"
                        + ".appendTo(container)."
                        + name + "Widget(options, "
                        + "{'pageWidget': pageWidget, 'condition': condition})"
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
        this._setOptions(this.options);
    },

    validate: function() {
        return true;
    },

    checkCondition: function() {
        if (this.options.condition != null) {
            if (this.options.condition())
                this._show(this.element, this.options.show, function(){});
            else
                this._hide(this.element, this.options.hide, function(){});
        }
    }

});

