iss.lib.widgets.SurveyWidget = function(options) {
    return function(condition) {
        if (condition()) {
            return function() {
                return {
                        "destination": options.destination(),
                        "name": options.name(),
                        "container": options.container()
                    };
            }
        }
        else {
            return function() {
                return null;
            }
        }
    }
}
