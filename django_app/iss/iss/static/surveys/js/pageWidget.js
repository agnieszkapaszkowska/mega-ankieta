iss.lib.widgets.PageWidget = function(options) {
    return function(condition) {  
        return function(questions, index) {
            return function(container) {
                    if (condition())
                        return $('<div id="' + index + '"></div>')
                            .appendTo(container)
                            .pageWidget(options, {
                                'questions': questions,
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
        questions: [],
        index: 0,
        buttons: function() { return true },
        nextbuttontext: function() { return "Next" },
        prevbuttontext: function() { return "Prev" },
    },
    
    _create: function() {
        this.element.addClass('page-widget');
        this._questionsContainer = $('<div></div>').appendTo(this.element);
        this._navigationContainer = $("<div></div>").appendTo(this.element);
        this._setOptions(this.options);
        if (this.options.buttons())
            this._setNavigationButtons();
    },

    _setOption: function(key, value) {
        if (key == 'questions')
            this._setQuestions(value);
        this._super(key, value);
    },

    _setQuestions: function(questions) {
        this._questionsContainer.find('div').remove();
        this.questions = [];
        this.notExecuted = [];
        for (var i = 0; i < questions.length; i++) {
            var question = questions[i](this._questionsContainer, this);
            if (question == null) {
                var div = $('<div></div>').appendTo(this._questionsCOntainer);
                this.notExecuted.push({question: questions[i], div: div});
            }
            else
                this.questions.push(question);
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
        for (var i = 0; i < this.questions.length; i++) {
            if (!this.questions[i].validate())
                return false;
        }
        return true;
    },

    childChanged: function() {
        for (var i = 0; i < this.questions.length; i++) {
            this.questions[i].checkCondition();
        }
        var newNotExecuted = [];
        for (var i = 0; i < this.notExecuted.length; i++) {
            var question = this.notExecuted[i].question(this.notExecuted[i].div, this);
            if (question == null)
                newNotExecuted.push(this.notExecuted[i]);
            else
                this.questions.push(question);
        }
        this.notExecuted = newNotExecuted;
    },

    getSubmitData: function() {
        var submitData = {};
        for (var i = 0; i < this.questions.length; i++) {
            submitData[i] = this.questions[i].getSubmitData();
        }
        return submitData;
    }
    
});

