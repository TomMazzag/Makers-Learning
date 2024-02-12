class Introducer {
    let name: String
    
    init(name: String) {
        self.name = name
    }
    
    func announce() -> String {
        return("I am \(name)!")
    }
    
    func introduce(who: String) -> String {
        return("Hello \(who), I am \(name)!")
    }
}

var introducer = Introducer(name: "Josué")

print(introducer.announce())
// Should print: "I am Josué!"

print(introducer.introduce(who: "Fred"))
// Should print: "Hello Fred, I am Josué!"

class Reminder {
    let name: String
    var reminders: [String]
    
    init(name: String) {
        self.name = name
        self.reminders = []
    }
    
    func remindMeTo(task: String) {
        reminders.append(task)
    }
    
    func remind() -> String {
        var remindString = "\(name)!"
        for reminder in reminders {
            remindString += " \(reminder)!"
        }
        return remindString
    }
}

var reminder = Reminder(name: "Josué")

reminder.remindMeTo(task: "Walk the dog")

print("")
print(reminder.remind())
// Should print: "Josué! Walk the dog!"


