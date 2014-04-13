$.widget("iss.likertWidget", $.iss.widget, {
    options: {
        questionWidget: null,
        condition: null,
        name: function() { return "" },
        data: function() { return {} },
        answers: function() {return [] },
        required: function() {return false },
        resultVarName: null
    },

    _create: function() {
        this._super();
    },

    _setOption: function(key, value) {
        if (key == "data")
            this._setData(value);
        else if (key == "resultVarName" && value != null)
            this._setCallback(value);
        this._super(key, value);
    },

    _setData: function(dataFun) {
        this.element.empty();
        var data = dataFun();
        this.questions = [];
        this.answers = this.options.answers();
        this.questionCount = 0;
        while (data[this.questionCount] != undefined) {
            var question = data[this.questionCount]();
            this.questions.push(question);
            this.questionCount ++;
        }
        $('<table id="' + this.options.name() + '"></table>')
            .appendTo(this.element);
        this._addHead();
        for (var i = 0; i < this.questionCount; i++) {
            this._addRow(i);
        }
    },

    _addHead: function() {
        var head = $('<tr></tr>').appendTo(this.element.find('table'));

        $('<th></th>').appendTo(head);
        for (var i = 0; i < this.answers.length; i++) {
            $('<th>' + this.answers[i]() + '</th>')
                .appendTo(head);
        }
    },

    _addRow: function(index) {
        var row = $('<tr></tr>').appendTo(this.element.find('table'));
        
        $('<td>' + this.questions[index].text() + '</td>').appendTo(row)
        for (var i = 0; i < this.answers.length; i++) {
            $('<td>' + this._addAnswerCell(i, index) + '</td>')
                .appendTo(row);
        }
    },

    _addAnswerCell: function(index, questionIndex) {
        var cell = '<input type="radio" name = "'
                   + this.questions[questionIndex].id()
                   + '" id = "' + this.questions[questionIndex].id()
                   + '_' + index + '" >'
        return cell;
    },

    _setCallback: function(varName) {
        iss.vars[varName] = [];
        var number = this.questions.length;
        while (number--) iss.vars[varName].push(-1);
        var element = this.element;
        var questionWidget = this.options.questionWidget;
        element.find('input').click(
            function() {
                var checked = [];
                element.find('tr').each(function() {
                    checked.push($(this).find('input')
                            .index($(this).find('input:checked')));
                });
                checked.shift();
                iss.vars[varName] = checked;
                questionWidget.childChanged();
            });
    },
    
    validate: function() {
        if (this.options.required()
            && this.element.is(":visible")
            && this.element.find('input:checked').length < this.questions.length) {
            this.element.addClass('erorr');
            return false;
        }
        return true;
    },
    
    insertSubmitData: function(submitData) {
        if(this.containsSubmitData) {
            var checked = [];
            var answers = this.answers;
            this.element.find("input:checked").each(function () {
                checked.push(answers[$(this).parent().index() - 1]());
            });
            submitData[this.options.name()] = checked;
        }
    }

});

