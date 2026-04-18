# LifeTwin – Personal Digital Twin Dashboard

This project represents a UI concept for a personal digital twin system.

## Features
- Tracks sleep, energy, and stress
- Shows digital twin sync status
- Provides AI-powered insights

## How it works
The system uses inputs like sleep, energy, and stress and processes them to generate insights.

## LPI Tools (Conceptual)
- smile_overview
- query_knowledge
- analyze_patterns

## Setup
This is a design prototype created in Figma.

## Example Insight
Input: Sleep = 6h, Energy = Low  
Output: “Your energy dips after 2 PM, consider taking a short break.”

## Error Handling

The agent checks for invalid inputs such as missing or negative values and returns appropriate messages.

## Example

Input: sleep=5, energy=4, stress=6  
Output: "Your energy may drop in the afternoon. Consider rest."

## Code Example

The agent calls multiple tools:

- smile_overview()
- query_knowledge()
- analyze_patterns()

It also includes error handling using try/except blocks to ensure stability.

## LPI Tool Integration

The agent uses subprocess to communicate with the LPI sandbox via Node.js.

It calls:
- smile_overview
- query_knowledge

These calls retrieve real outputs from the LPI system.
