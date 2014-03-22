iss.lib.Survey = function() {
    this.pages = [];
    this.currentPage = null;
    this.currentIndex = 0;
    this.conditions = [];
    this.widgets = [];
    this.assignments = [];
    this.container = "#image .panel-body";
    this.history = [];
    
    this.addAssignment = addAssignment;
    this.addWidget = addWidget;
    this.addWidgetConditional = addWidgetConditional;
    this.init = init;
    this.addPage = addPage;
    this.gotoNext = gotoNext;
    this.gotoPrev = gotoPrev;
    this.prepareCondition = prepareCondition;
    this.submit = submit;
    
    function addAssignment(fun) {
        var condFun = this.prepareCondition(this.conditions.slice(0));
        this.assignments.push(function() { if (condFun()) fun(); });
    }

    function addWidget(fun) {
        var condFun = this.prepareCondition(this.conditions.slice(0));
        var newFunction = fun()(condFun);
        if (fun.toString().indexOf(
                "iss.lib.widgets.PageWidget") != -1) {
            this.addPage();   
            this.currentPage = newFunction;
        }
        else {
            this.widgets.push(newFunction);
        }
    }

    function addWidgetConditional(array) {
        for (var i = 0; i < array.length; i++) {
            this.conditions.push(array[i].condition);
            array[i].body();
            this.conditions.pop();
        }
    }

    function prepareCondition(conditions) {
        return function() {
            for (var i = 0; i < conditions.length; i++)
                if (!conditions[i]())
                    return false;
            return true;
        }
    }

    function addPage() {
        if (this.currentPage != null) {
            this.pages.push(this.currentPage(
                this.widgets, this.assignments, this.currentIndex));
        }
        else if (this.widgets.length > 0) {
            this.pages.push(iss.lib.widgets.PageWidget({})(
                this.prepareCondition(this.conditions.slice(0)))(
                this.widgets, this.assignments, this.currentIndex));
        }
        this.widgets = [];
        this.assignments = [];
        this.currentIndex ++;
    }
    
    function init() {
        this.addPage();
        this.currentIndex = -1;
        this.gotoNext();
    }

    function gotoNext() {
        if (this.history.length > 0) {
            if (this.history[this.history.length - 1].widget.validatePage())
                this.history[this.history.length - 1].widget.hide();
            else {
                console.log("Did not validate");
                return;
            }
        }
        var widget = null;
        while (widget == null
               && this.currentIndex < this.pages.length - 1) {
            this.currentIndex ++;
            widget = this.pages[this.currentIndex](this.container);
        }
        if (widget == null) {
            this.submit();
            return;
        }
        this.history.push({
            widget: widget,
            index: this.currentIndex});
    }

    function gotoPrev() {
        this.history.pop().widget.destroy();
        if (this.history.length > 0)
            this.history[this.history.length - 1].widget.show();
            this.currentIndex = this.history[this.history.length - 1].index;
    }

    function submit() {
        return;
    }
}
