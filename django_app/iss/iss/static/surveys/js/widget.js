iss.lib.widgets.Widget = function(name, options) {
    return function(condition) {
        return function(container) {
                if (condition())
                    return eval("$('<div></div>')"
                        + ".appendTo(container)."
                        + name + "Widget(options)"
                        + ".data('iss-' + name + '-widget')");
                return null;
               }
           }
}

$.widget("iss.widget", {
    options: {},

    _create: function() {
        this.element.addClass(this.widgetName);
        this._setOptions(this.options);
    },

    validate: function() {
        return true;
    }

});

