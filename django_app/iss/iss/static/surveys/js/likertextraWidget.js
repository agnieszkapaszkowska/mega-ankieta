$.widget("iss.likertextraWidget", $.iss.widget, {
    options: {
        questionWidget: null,
        condition: null,
        name: function() { return "" },
        data: function() { return [] },
        question: function() { return "" },
        title: function() { return "" },
        answers: function() {return [] },
        required: function() {return true },
        resultVarName: null,
        tupleArgs: {
            id: function() { return "" }, 
            text: function() { return "" }
        }
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
        for (var i = 0; i < data.length; i++) {
            var question = data[i]();
            this.updateTupleArgs(question, this.options.tupleArgs);
            this.questions.push(question);
        }
        $('<table id="' + this.options.name() + '"></table>')
            .appendTo(this.element);
        this._addHead();
        for (var i = 0; i < this.questions.length; i++) {
            this._addRow(i);
        }
    },

    _addHead: function() {
        var head = $('<tr></tr>').appendTo(this.element.find('table'));

        $('<th style="width: 25%;">' + this.options.title() + '</th>').appendTo(head);
        var width = 75 / (this.answers.length + 1);
        for (var i = 0; i < this.answers.length; i++) {
            $('<th style="width:' + width + '%;">' + this.answers[i]() + '</th>')
                .appendTo(head);
        }
        $('<th style="width:' + width + '%;">' + this.options.question() + '</th>').appendTo(head);
    },

    _addRow: function(index) {
        var row = $('<tr></tr>').appendTo(this.element.find('table'));
        
        $('<td>' + this.questions[index].text() + '</td>').appendTo(row)
        for (var i = 0; i < this.answers.length; i++) {
            $('<td>' + this._addAnswerCell(i, index) + '</td>')
                .appendTo(row);
        }
        this._addExtraCell(index, row);
    },

    _addAnswerCell: function(index, questionIndex) {
        var cell = '<input type="radio" name = "'
                   + this.questions[questionIndex].id()
                   + '" id = "' + this.questions[questionIndex].id()
                   + '_' + index + '" >'
        return cell;
    },

    _getChecked: function() {
        var result = {};
        var answers = this.answers;
        var widget = this;
        this.element.find('tr').each(function() {
            var input = $(this).find('input');
            var index = input.index($(this).find('input:checked'));
            if (index == -1)
                result[input.attr("name")] = null;
            else
                result[input.attr("name")] = answers[index]();
            result[input.attr("name") + "_extra"] = widget._getExtraValue($(this));
        });
        return result;
    },

    _existsEmptyField: function() {
        this.element.find('tr').removeClass('error');
        var widget = this;
        var result = false;
        var first = true;
        this.element.find('tr').each(function() {
            if (first) {
                first = false;
            }
            else {
                var input = $(this).find('input');
                var index = input.index($(this).find('input:checked'));
                if (!result && (index == -1 || !widget._checkExtraValue($(this)))) {
                    $(this).addClass('error');
                    result = true;
                }
            }
        });
        return result;
    },

    _setCallback: function(varName) {
        iss.vars[varName] = this._getChecked();
        var that = this;
        var questionWidget = this.options.questionWidget;
        this.element.find('input').change(
            function() {
                iss.vars[varName] = that._getChecked();
                questionWidget.childChanged();
            });
    },
    
    validate: function() {
        if (this.options.required()
                && this.element.is(":visible")
                && this._existsEmptyField()) {
            return false;
        }
        this.element.removeClass("error");
        return true;
    },
    
    insertSubmitData: function(submitData) {
        if(this.containsSubmitData) {
            submitData[this.options.name()] = this._getChecked();
        }
    }

});

