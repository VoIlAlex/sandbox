#include <cstdlib>
#include <iostream>
#include <streambuf>
#include <string>
#include <sstream>
#include <stdio.h>

std::string to_lower(std::string &str)
{
    std::string result;
    for (char &ch : str)
        result += tolower(ch);
    return result;
}

class BShell
{
    std::istream &m_in;
    std::ostream &m_out;

public:
    BShell(std::istream &stream_in, std::ostream &stream_out);
    void main_loop();

private:
    // TODO: remove (on demand)
    bool run_without_error(const std::string &command);
};

main()
{
    BShell(std::cin, std::cout).main_loop();
}

BShell::BShell(std::istream &stream_in, std::ostream &stream_out)
    : m_in(stream_in), m_out(stream_out)
{
    //m_out << "Welcome to bshell!" << std::endl;
}

void BShell::main_loop()
{
    std::string command;
    char output[1024] = "";
    while (true)
    {
        std::cout << ":>";
        std::cin >> command;

        if (to_lower(command) == "exit")
            return;

        FILE *pOutput = popen(command.c_str(), "r");
        if (pOutput == NULL)
        {
            m_out << "Bay!" << std::endl;
            break;
        }

        while (fgets(output, 1024, pOutput))
            std::cout << output;
    }
}

bool BShell::run_without_error(const std::string &command)
{
    // redirect output
    std::streambuf *buff = m_out.rdbuf();
    std::ostringstream output;
    m_out.rdbuf(output.rdbuf());
    // run command
    if (system(command.c_str()))
        return false;
    // if command exits with
    // the returned value
    // equal to 0 (everything okay)
    return true;
}