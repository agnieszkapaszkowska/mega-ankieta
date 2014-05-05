iss.lib.widgets.QuestionWidget = function(options) {
    return function(condition) {  
        return function(widgets, assignments) {
            return function(container, pageWidget) {
                    if (condition())
                        return $('<div></div>')
                            .appendTo(container)
                            .questionWidget(options, {
                                'condition': condition,
                                'widgets': widgets,
                                'assignments': assignments,
                                'pageWidget': pageWidget})
                            .data('iss-question-widget');
                     return null;
                   }
               }
           }
}

$.widget("iss.questionWidget", {
    options: {
        condition: null,
        assignments: [],
        widgets: [],
        pageWidget: null
    },
    
    _create: function() {
        this.element.addClass('question-widget');
        this._widgetsContainer = $('<div></div>').appendTo(this.element);
        this._setOptions(this.options);
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

    validate: function() {
        for (var i = 0; i < this.widgets.length; i++) {
            if (!this.widgets[i].validate())
                return false;
        }
        return true;
    },

    checkCondition: function() {
        if (this.options.condition != null) {
            if (this.options.condition()) {
                this._show(this.element, this.options.show, function(){});
                this.checkChildren();
            }
            else
                this._hide(this.element, this.options.hide, function(){});
        }
    },

    checkChildren: function() {
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
    },

    childChanged: function() {
        if (this.options.pageWidget != null)
            this.options.pageWidget.childChanged();
    },

    getSubmitData: function() {
        var submitData = {};
        for (var i = 0; i < this.widgets.length; i++) {
            this.widgets[i].insertSubmitData(submitData);
        }
        return submitData;
    }
    
});

