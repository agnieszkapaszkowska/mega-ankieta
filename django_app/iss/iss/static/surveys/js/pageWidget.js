iss.lib.widgets.PageWidget = function(options) {
    return function(widgets, index) {
        return function(container) {
                return $('<div id="' + index + '"></div>')
                    .appendTo(container)
                    .pageWidget(options, {
                        'widgets': widgets,
                        'index': index})
                    .data('iss-page-widget');
               }
           }
}

$.widget("iss.pageWidget", {
    options: {
        back: function() { return false },
        widgets: [],
        index: 0
    },
    
    _create: function() {
        this.element.addClass('page-widget');
        this._widgetsContainer = $('<div></div>').appendTo(this.element);
        this._navigationContainer = $("<div></div>").appendTo(this.element);
        this._setOption('widgets', this.options.widgets);
        this._setNavigationButtons();
    },

    _setOption: function(key, value) {
        if (key == 'widgets')
            this._setWidgets(value);
        this._super(key, value);
    },

    _setWidgets: function(widgets) {
        this._widgetsContainer.find('div').remove();
        for (var i = 0; i < widgets.length; i++) {
            widgets[i](this._widgetsContainer);
        }
    },

    _setNavigationButtons: function() {
        if (this.options.back())
            $('<button onclick="iss.survey.gotoPrev()">Back</button>')
                .appendTo(this._navigationContainer);
        $('<button onclick="iss.survey.gotoNext()">Next</button>')
            .appendTo(this._navigationContainer);
    },

    hide: function() {
        this._hide(this.element, this.options.hide, function(){});
    },

    show: function() {
        this._show(this.element, this.options.show, function(){});
    },

    _destroy: function() {
        this.element.removeClass('page-widget');
        this.element.empty();
    }
});

