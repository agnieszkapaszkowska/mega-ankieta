iss.lib.Survey = function() {
    this.pages = [];
    this.currentPage = null;
    this.currentIndex = 0;
    this.widgets = [];
    this.container = "#image .panel-body";
    this.history = [];
    
    this.addAssignment = addAssignment;
    this.addWidget = addWidget;
    this.addWidgetConditional = addWidgetConditional;
    this.init = init;
    this.addPage = addPage;
    this.getNextIndex = getNextIndex;
    this.gotoNext = gotoNext;
    this.gotoPrev = gotoPrev;
    
    function addAssignment(fun) {
        fun();
    }

    function addWidget(fun) {
        var newFunction = fun();
        if (fun.toString().indexOf(
                "iss.lib.widgets.PageWidget") != -1) {
            this.addPage();   
            this.currentPage = newFunction;
        }
        else {
            this.widgets.push(newFunction);
        }
    }

    function addWidgetConditional(fun) {
        console.log("WidgetConditional");
    }

    function addPage() {
        if (this.currentPage != null) {
            this.pages.push(this.currentPage(
                this.widgets, this.currentIndex));
        }
        else if (this.widgets.length > 0) {
            this.pages.push(iss.lib.widgets.PageWidget({})(
                this.widgets, this.currentIndex));
        }
        this.widgets = [];
        this.currentIndex ++;
    }
    
    function init() {
        this.addPage();
        this.currentIndex = -1;
        this.gotoNext();
    }

    function getNextIndex(index) {
        return index + 1;
    }

    function gotoNext() {
        if (this.history.length > 0)
            this.history[this.history.length - 1].widget.hide();
        this.currentIndex = this.getNextIndex(this.currentIndex);
        this.history.push({
            widget: this.pages[this.currentIndex](this.container),
            index: this.currentIndex});
    }

    function gotoPrev() {
        this.history.pop().widget.destroy();
        if (this.history.length > 0)
            this.history[this.history.length - 1].widget.show();
            this.currentIndex = this.history[this.history.length - 1].index;
    }
}
