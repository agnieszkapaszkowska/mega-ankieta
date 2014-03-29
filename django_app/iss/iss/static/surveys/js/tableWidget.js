$.widget("iss.tableWidget", $.iss.widget, {
    options: {
        questionWidget: null,
        condition: null,
        name: '',
        data: function() { return {} },
        number: function() {return 0 },
        required: function() {return false },
        resultVarName: null
    },

    _create: function() {
        this._super();
    },

    _setOption: function(key, value) {
        if (key == "data")
            this._setData(value);
        this._super(key, value);
    },

    _setData: function(dataFun) {
        this.element.empty();
        var data = dataFun();
        this.lists = [];
        this.minLength = -1;
        var i = 0;
        while (data[i] != undefined) {
            var list = data[i]();
            if (this.minLength == -1 || list.length < this.minLength)
                this.minLength = list.length;
            this.lists.push(list);
            i ++;
        }
        $('<table id="' + this.options.name() + '"></table>')
            .appendTo(this.element);
        this.nextIndex = Math.min(this.options.number(), this.minLength);
        for (var i = 0; i < this.nextIndex; i++) {
            this._addRow(i);
        }
        this._addButtons();
    },

    _addRow: function(index) {
        var row = $('<tr></tr>').appendTo(this.element.find('table'));
        for (var i = 0; i < this.lists.length; i++) {
            $('<td>' + this.lists[i][index]() + '</td>')
                .appendTo(row);
        }
    },

    _addButtons: function() {
        var buttonNext = $('<button>Show Next</button>')
            .appendTo(this.element);
        var buttonEnd = $('<button>Finish</button>')
            .appendTo(this.element);
        var that = this;
        buttonNext.click(function() {
            that._addRow(that.nextIndex);
            that.nextIndex ++;
            if (that.nextIndex >= that.minLength)
                buttonNext.hide();
        });
        buttonEnd.click(function() {
            iss.survey.gotoNext();
        });
        if (this.nextNumber >= this.minLength)
            buttonNext.hide();
    },

});

