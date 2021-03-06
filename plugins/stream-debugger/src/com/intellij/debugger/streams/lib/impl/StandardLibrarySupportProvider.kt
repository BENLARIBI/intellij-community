/*
 * Copyright 2000-2017 JetBrains s.r.o.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package com.intellij.debugger.streams.lib.impl

import com.intellij.debugger.streams.lib.LibrarySupport
import com.intellij.debugger.streams.lib.LibrarySupportProvider
import com.intellij.debugger.streams.psi.impl.JavaChainTransformerImpl
import com.intellij.debugger.streams.psi.impl.JavaStreamChainBuilder
import com.intellij.debugger.streams.trace.TraceExpressionBuilder
import com.intellij.debugger.streams.trace.dsl.Dsl
import com.intellij.debugger.streams.trace.dsl.impl.DslImpl
import com.intellij.debugger.streams.trace.dsl.impl.java.JavaStatementFactory
import com.intellij.debugger.streams.trace.impl.JavaTraceExpressionBuilder
import com.intellij.debugger.streams.wrapper.StreamChainBuilder
import com.intellij.openapi.project.Project

/**
 * @author Vitaliy.Bibaev
 */
class StandardLibrarySupportProvider : LibrarySupportProvider {
  private companion object {
    val builder: StreamChainBuilder = JavaStreamChainBuilder(JavaChainTransformerImpl(), "java.util.stream")
    val support: LibrarySupport = StandardLibrarySupport()
    val dsl: Dsl = DslImpl(JavaStatementFactory())
  }

  override fun getLanguageId(): String = "JAVA"

  override fun getExpressionBuilder(project: Project): TraceExpressionBuilder =
    JavaTraceExpressionBuilder(project, support.createHandlerFactory(dsl))

  override fun getChainBuilder(): StreamChainBuilder = builder

  override fun getLibrarySupport(): LibrarySupport = support
}
