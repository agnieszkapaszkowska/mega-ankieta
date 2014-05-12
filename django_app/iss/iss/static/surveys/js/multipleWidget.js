$.widget("iss.multipleWidget", $.iss.widget, {
    options: {
        questionWidget: null,
        condition: null,
        name: function() { return "" },
        title: function() { return "" },
        answers: function() {return [] },
        questions: function() { return [] },
        required: function() {return true },
        resultVarName: null,
        tupleArgs: {
            id: function() { return "" }, 
            text: function() { return "" }
        }
    },

    _create: function() {
        this._super();
        this._drawTable();
    },

    _setOption: function(key, value) {
        if (key == "questions") {
            this.questions = [];
            this._setData(value, this.questions);
        }
        else if (key == "answers") {
            this.answers = [];
            this._setData(value, this.answers);
        }
        else if (key == "resultVarName" && value != null)
            this._setCallback(value);
        this._super(key, value);
    },

    _setData: function(fun, variable) {
        var data = fun();
        for (var i = 0; i < data.length; i++) {
            var dataElem = data[i]();
            this.updateTupleArgs(dataElem, this.options.tupleArgs);
            variable.push(dataElem);
        }
    },
   
    _drawTable: function() {
        this.element.empty(); 
        $('<table id="' + this.options.name() + '"></table>')
            .appendTo(this.element);
        this._addHead();
        for (var i = 0; i < this.questions.length; i++) {
            this._addRow(i);
        }
    },

    _addHead: function() {
        var head = $('<tr></tr>').appendTo(this.element.find('table'));

        $('<th>' + this.options.title() + '</th>').appendTo(head);
        for (var i = 0; i < this.answers.length; i++) {
            $('<th>' + this.answers[i].text() + '</th>')
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
        return '<input style="width:50px;" type="number" id ="' + this.options.name() + '_'
                + questionIndex + '_' + index + '">';
    },

    _getData: function() {
        var result = {};
        var name = this.options.name();
        for (var i = 0; i < this.questions.length; i++) {
            var row = {};
            for (var j = 0; j < this.answers.length; j++)
                row[this.answers[j].id()] = $('#' + name + '_' + i + '_' + j).val();
            result[this.questions[i].id()] = row;
        }
        return result;
    },

    _existsEmpty: function() {
        var name = this.options.name();
        for (var i = 0; i < this.questions.length; i++)
            for (var j = 0; j < this.answers.length; j++)
                if ($('#' + name + '_' + i + '_' + j).val().length == 0)
                    return true;
        return false;
    },

    _setCallback: function(varName) {
        iss.vars[varName] = this._getData();
        console.log(iss.vars[varName]);
        var questionWidget = this.options.questionWidget;
        var that = this;
        this.element.find('input').change(
            function() {
                iss.vars[varName] = that._getData();
                questionWidget.childChanged();
            });
    },
    
    validate: function() {
        if (this.options.required()
            && this.element.is(":visible")
            && this._existsEmptyField()) {
            this.element.addClass('erorr');
            return false;
        }
        return true;
    },
    
    insertSubmitData: function(submitData) {
        if(this.containsSubmitData) {
            submitData[this.options.name()] = this._getData();
        }
    }

});

