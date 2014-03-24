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
        assignments: [],
        widgets: [],
        index: 0,
        buttons: function() { return true },
        nextbuttontext: function() { return "Next" },
        prevbuttontext: function() { return "Prev" },
    },
    
    _create: function() {
        this.element.addClass('page-widget');
        this._widgetsContainer = $('<div></div>').appendTo(this.element);
        this._navigationContainer = $("<div></div>").appendTo(this.element);
        this._setOptions(this.options);
        if (this.options.buttons())
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
        this.widgets = [];
        this.notExecuted = [];
        for (var i = 0; i < widgets.length; i++) {
            var widget = widgets[i](this._widgetsContainer, this);
            if (widget == null)
                this.notExecuted.push(widgets[i]);
            else
                this.widgets.push(widget);
        }
    },
    
    _setAssignments: function(assignments) {
        for (var i = 0; i < assignments.length; i++) {
            assignments[i]();
        }
    },

    _setNavigationButtons: function() {
        if (this.options.back())
            $('<button onclick="iss.survey.gotoPrev()">'
                    + this.options.prevbuttontext() + '</button>')
                .appendTo(this._navigationContainer);
        $('<button onclick="iss.survey.gotoNext()">'
                    + this.options.nextbuttontext() + '</button>')
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
    },

    validatePage: function() {
        for (var i = 0; i < this.widgets.length; i++) {
            if (!this.widgets[i].validate())
                return false;
        }
        return true;
    },

    childChanged: function() {
        for (var i = 0; i < this.widgets.length; i++) {
            this.widgets[i].checkCondition();
        }
        var newNotExecuted = [];
        for (var i = 0; i < this.notExecuted.length; i++) {
            var widget = this.notExecuted[i](this._widgetsContainer, this);
            if (widget == null)
                newNotExecuted.push(this.notExecuted[i]);
            else
                this.widgets.push(widget);
        }
        this.notExecuted = newNotExecuted;
    }
    
});

