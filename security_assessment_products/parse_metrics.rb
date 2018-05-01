require 'json'

assessment_metrics = JSON.parse(File.read("assessments.json"))

puts "Maximum: " + assessment_metrics.map {|h| h["whiteboard"]}.map {|w| w["MAXIMUM"].to_i}.sum.to_s
puts "High: " + assessment_metrics.map {|h| h["whiteboard"]}.map {|w| w["HIGH"].to_i}.sum.to_s
puts "Medium: " + assessment_metrics.map {|h| h["whiteboard"]}.map {|w| w["MEDIUM"].to_i}.sum.to_s
puts "Low: " + assessment_metrics.map {|h| h["whiteboard"]}.map {|w| w["LOW"].to_i}.sum.to_s

automation_metrics = JSON.parse(File.read("automation.json"))

puts "Maximum: " + automation_metrics.map {|h| h["whiteboard"]}.map {|w| w["MAXIMUM"].to_i}.sum.to_s
puts "High: " + automation_metrics.map {|h| h["whiteboard"]}.map {|w| w["HIGH"].to_i}.sum.to_s
puts "Medium: " + automation_metrics.map {|h| h["whiteboard"]}.map {|w| w["MEDIUM"].to_i}.sum.to_s
puts "Low: " + automation_metrics.map {|h| h["whiteboard"]}.map {|w| w["LOW"].to_i}.sum.to_s