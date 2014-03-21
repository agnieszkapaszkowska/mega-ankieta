iss.lib.widgets.PageWidget = function(options) {
    return function(condition) {  
        return function(widgets, assignments, index) {
            return function(container) {
                    if (condition())
                        return $('<div id="' + index + '"></div>')
                            .appendTo(container)
                            .pageWidget(options, {
                                'widgets': widgets,
                                'assignments': assignments,
                                'index': index})
                            .data('iss-page-widget');
                     return null;
                   }
               }
           }
}

$.widget("iss.pageWidget", {
    options: {
        back: function() { return false },
        widgets: [],
        assignments: [],
        index: 0
    },
    
    _create: function() {
        this.element.addClass('page-widget');
        this._widgetsContainer = $('<div></div>').appendTo(this.element);
        this._navigationContainer = $("<div></div>").appendTo(this.element);
        this._setOptions(this.options);
        this._setNavigationButtons();
    },

    _setOption: function(key, value) {
        if (key == 'widgets')
            this._setWidgets(value);
        else if (key == 'assignments')
            this._setAssignments(value);
        this._super(key, value);
    },

    _setWidgets: function(widgets) {
        this._widgetsContainer.find('div').remove();
        for (var i = 0; i < widgets.length; i++) {
            widgets[i](this._widgetsContainer);
        }
    },
    
    _setAssignments: function(assignments) {
        for (var i = 0; i < assignments.length; i++) {
            assignments[i]();
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

